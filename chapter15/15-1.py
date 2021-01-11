import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, lw=1)
    plt.scatter(0, 0, c = 'red', s = 30) # 绘制起点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', s = 30) # 绘制终点
    plt.axes().get_xaxis().set_visible(False) # 隐藏坐标轴
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break