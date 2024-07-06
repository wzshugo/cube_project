import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

s2_values = np.linspace(0.5, 10.5, num=20)
data = []

for s2 in s2_values:
    m1 = 25
    s1 = 1.5
    m2 = 32
    p1 = m1 + s1 * np.random.randn(720)
    p2 = m2 + s2 * np.random.randn(720)
    new_p1 = []
    new_p2 = []
    M1 = []
    M2 = []
    new_m1 = 0
    new_m2 = 0
    p = np.concatenate((p1, p2), axis=0)
    M1.append(m1)
    M2.append(m2)

    while abs(new_m1 - m1) > 1e-3 and abs(new_m2 - m2) > 1e-3:
        new_p1.clear()
        new_p2.clear()
        if new_m1 != 0:
            m1 = new_m1
        if new_m2 != 0:
            m2 = new_m2
        for i in p:
            if abs(i - m1) <= abs(i - m2):
                new_p1.append(i)
            else:
                new_p2.append(i)
        new_m1 = sum(new_p1) / len(new_p1)
        new_m2 = sum(new_p2) / len(new_p2)
        M1.append(new_m1)
        M2.append(new_m2)

    data.append((s2, M1, M2))

# 绘制三维坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 创建颜色映射
color_map1 = cm.get_cmap('Reds')
color_map2 = cm.get_cmap('Blues')

# 绘制数据
for i, (s2, M1, M2) in enumerate(data):
    x = range(len(M1))
    y = [s2] * len(M1)
    color1 = color_map1(i / len(data))  # 根据索引获取颜色
    color2 = color_map2(i / len(data))
    ax.plot(x, y, M1, color=color1, label=f'person1 (s2={s2:.1f})')
    ax.plot(x, y, M2, color=color2, label=f'person2 (s2={s2:.1f})')

# 设置坐标轴标签
ax.set_xlabel('Index')
ax.set_ylabel('s2')
ax.set_zlabel('average temperature')
ax.set_title('change of average temperature by s2')

# 设置图例
ax.legend(loc = 'upper right')

# 显示图形
plt.show()