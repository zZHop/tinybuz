import matplotlib.pyplot as plt
import numpy as np

def generate_101st_clause_logo():
    # 颜色定义
    bg_color = '#0A1931'    # 午夜蓝
    line_color = '#FADADD'  # 羊毛粉
    text_color = '#E2E2E2'  # 极轻的银灰

    # 设置画布
    fig, ax = plt.subplots(figsize=(10, 10), facecolor=bg_color)
    ax.set_facecolor(bg_color)

    # 1. 绘制外围的 100 个度量刻度 (The Rules)
    r_outer = 1.1
    r_inner = 1.05
    for i in range(101):
        angle = i * (2 * np.pi / 100)
        # 顶部留出 30 度的缺口 (给第 101 只羊)
        if 0.42 * np.pi < angle < 0.58 * np.pi:
            continue
        
        x_start, y_start = r_inner * np.cos(angle), r_inner * np.sin(angle)
        x_end, y_end = r_outer * np.cos(angle), r_outer * np.sin(angle)
        
        # 刻度粗细分级
        lw = 0.8 if i % 10 == 0 else 0.4
        alpha = 0.6 if i % 10 == 0 else 0.3
        ax.plot([x_start, x_end], [y_start, y_end], color=line_color, lw=lw, alpha=alpha)

    # 2. 绘制核心符号 § (Stylized Section Symbol)
    # 使用参数方程构建几何化的 §
    t = np.linspace(0, 2 * np.pi, 500)
    
    # 下半圆弧
    x_bottom = 0.3 * np.cos(t[150:450])
    y_bottom = 0.3 * np.sin(t[150:450]) - 0.35
    ax.plot(x_bottom, y_bottom, color=line_color, lw=1.5, alpha=0.9)
    
    # 中间连接线
    ax.plot([0.3*np.cos(1.8*np.pi), 0.3*np.cos(0.8*np.pi)], 
            [0.3*np.sin(1.8*np.pi)-0.35, 0.3*np.sin(0.8*np.pi)+0.35], 
            color=line_color, lw=1.2, alpha=0.7)

    # 3. 绘制羊角 (The Yang / Fibonacci Horns)
    # 羊角从 § 的顶部螺旋散开
    def spiral(a, b, t_range, offset_x, offset_y, direction=1):
        theta = np.linspace(t_range[0], t_range[1], 100)
        x = a * np.exp(b * theta) * np.cos(direction * theta) + offset_x
        y = a * np.exp(b * theta) * np.sin(direction * theta) + offset_y
        return x, y

    # 左角
    xl, yl = spiral(0.08, 0.22, [1, 5], -0.05, 0.5, direction=1)
    ax.plot(xl, yl, color=line_color, lw=2, alpha=1)
    # 右角
    xr, yr = spiral(0.08, 0.22, [1, 5], 0.05, 0.5, direction=-1)
    ax.plot(xr, yr, color=line_color, lw=2, alpha=1)

    # 4. 文字排版：全大写衬线风格
    # 主标题
    plt.text(0, -1.4, 'THE 101st CLAUSE', color=line_color, 
             fontsize=22, fontweight='light', ha='center', letterspacing=10)
    
    # 副标题：中文名 
    plt.text(0, -1.65, '第 1 0 1 条 条 款', fontfamily='SimSun', color=text_color, 
             fontsize=14, ha='center', alpha=0.5, letterspacing=5)

    # 底部 Slogan
    plt.text(0, -1.9, 'Logic for Dreamers', color=text_color, 
             fontsize=10, ha='center', fontstyle='italic', alpha=0.3)

    # 隐藏坐标轴，设置显示比例
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.axis('off')

    plt.title("Brand Identity Prototype v2.0", color=line_color, 
              fontsize=8, pad=20, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    try:
        generate_101st_clause_logo()
        print("§ 101 | 品牌 Logo 已在午夜蓝背景下生成。")
        print("视觉语言：极其纤细的粉色线条代表‘一扬’的羊毛质感，与冷峻的几何构图形成反差。")
    except Exception as e:
        print(f"生成失败: {e}")
