import matplotlib.pyplot as plt

# plt.figure()
# x=np.linspace(0,3,100)
# plt.subplot(221)
# plt.plot(x,np.exp(x/3))

# plt.subplot()
# #绘制柱状图
# # plt.figure()
# n = 18
# X = np.arange(n)+1 #X是1,2,3,4,5,6,7,8,柱的个数
# #uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
# Y1 = np.random.uniform(0.5,1.0,n)
# Y2 = np.random.uniform(0.5,1.0,n)
# plt.bar(X, Y1, width = 0.35, facecolor = 'lightskyblue')
# plt.bar(X+0.35, Y2,width = 0.35, facecolor = 'yellowgreen')
#
# plt.show()
import json


def Bubble_Sort(a):
    # plt.figure()

    for i in range(len(a) - 1):
        flag = True
        # print('-----第%d轮-----' % (i + 1))
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = False
            # 写文件
            my_file = open(file, 'a')
            for i in a:
                my_file.write(str(i))
            my_file.write('\n')
            my_file.close()
        if flag:
            break
            # print(a)


if __name__ == '__main__':
    a = [9, 3, 7, 6, 2, 8, 1]
    file = 'bubble.csv'
    Bubble_Sort(a)
    fig, ax = plt.subplots()
    # 读文件
    for line in open(file):
        result = line.strip()
        result1 = [int(x) for x in result]
        print(result1)
        print(len(result1))
        # 绘制柱形图
        # x = (1, 2, 3, 4, 5, 6,)
        plt.cla()

        ax.bar(x=range(len(a)), height=result1)
        plt.pause(0.3)

    plt.show()
    file.close()
# 绘制动态图
#
# from matplotlib import pyplot as plt
# from matplotlib import animation
# import numpy as np
# fig, ax = plt.subplots()
#
# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))
#     return line,
#
#
# def init():
#     line.set_ydata(np.sin(x))
#     return line,
#
#
# ani = animation.FuncAnimation(fig=fig,
#                               func=animate,
#                               frames=100,
#                               init_func=init,
#                               interval=20,
#                               blit=False)
#
#
# plt.show()
