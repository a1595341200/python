'''
Author: yao.xie 1595341200@qq.com
Date: 2023-07-11 12:35:06
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-07-11 12:35:21
FilePath: /python/高斯分布.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8

# plot Gaussian Function
# 注：正态分布也叫高斯分布
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Ellipse


# 生成一个高斯分布函数
def gaussianBlob(u, sigma):
    x = np.arange(-4, 4, 0.1)
    y = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma, -1), np.exp(-np.power(x - u, 2) / (2 * sigma ** 2)))
    return x, y


def setFigure():
    ax = plt.gca()
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['left'].set_position(('axes', 0))


def test():
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决pythonmatplotlib绘图无法显示中文的问题
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    us = np.arange(0, 5, 1)
    sigmas = np.arange(0.1, 1, 0.1)

    fig = plt.figure()
    plt.ion()

    while 1:
        count = 1
        for i in range(len(us)):
            for j in range(len(sigmas)):
                fig.clf()
                x, y = gaussianBlob(us[i], sigmas[j])
                plt.plot(x, y, linewidth=2, label=str('u=') + str(us[i]) + ',' + str('sigma=') + str(sigmas[j]))
                plt.plot([us[i], us[i]], [0, 1], color='r')
                plt.title("Gaussian blob")
                setFigure()
                if j != 0:
                    x, y = gaussianBlob(us[i], sigmas[j - 1])
                    plt.plot(x, y, linewidth=2, color='g',
                             label=str('u=') + str(us[i]) + ',' + str('sigma=') + str(sigmas[j - 1]))

                plt.legend()
                plt.pause(1)
            if i == 5:
                i = 0
    plt.ioff()
    plt.show()


def sigma():
    u0 = 0
    s0 = 1
    x, y = gaussianBlob(u0, s0)
    plt.plot(x, y, linewidth=2, label=(str('u=') + str(u0) + str(',sigma=') + str(s0)))
    u1 = 4
    s1 = 2
    x, y = gaussianBlob(u1, s1)
    plt.plot(x, y, linewidth=2, color='red', label=(str('u=') + str(u1) + str(',sigma=') + str(s1)))
    u = u0 + math.pow(s0, 2) * (u1 - u0) / (math.pow(s0, 2) + math.pow(s1, 2))
    s = math.pow(s0, 2) - math.pow(s0, 4) / (math.pow(s0, 2) + math.pow(s1, 2))
    x, y = gaussianBlob(u, s)
    plt.plot(x, y, linewidth=2, color='g', label=(str('u=') + str(u) + str(',sigma=') + str(s)))
    plt.legend()
    plt.show()


def plotEllipse(mu, cov, color):
    x, y = np.random.multivariate_normal(mu, cov, 1000).T
    # print(sigma)
    # 计算置信椭圆参数
    eigvals, eigvecs = np.linalg.eig(cov)
    index = 0
    max = 0
    print(mu)
    print(eigvals)
    for i in range(len(eigvals)):
        if (eigvals[i] >= max):
            max = eigvals[i]
            index = i
    print(index)
    # print(np.arctan2(*eigvecs[index]))
    print("eigvecs[index]", np.abs(eigvecs[index]))
    theta = 90 - np.degrees(np.arctan2(*np.abs(eigvecs[index])))
    print("theta", theta)
    print(2 * np.sqrt(abs(eigvals)))
    # width和height分别表示绘制的椭圆的宽度和高度。具体来说，它们是通过将椭圆的半长轴和半短轴的长度设置为：

    # 半长轴的长度等于2 * nstd * sqrt(eigenvalue_1)，其中eigenvalue_1是协方差矩阵的第一个特征值。
    # 半短轴的长度等于2 * nstd * sqrt(eigenvalue_2)，其中eigenvalue_2是协方差矩阵的第二个特征值。

    # 因此，width和height定义了椭圆的大小和形状，这取决于协方差矩阵的特征值以及nstd的值。当nstd = 1
    # 时，它们定义了一个标准偏差的椭圆，绘制的置信椭圆包含了数据的约68.27 % 的置信区间。

    # nstd = 2 表示椭圆的长度和宽度分别扩展到2倍标准差的大小，覆盖了大约95.45 % 的数据。这是因为在正态分布中，大约有
    # 95.45 % 的数据落在距离均值两个标准差的范围内。因此，使用 nstd = 2绘制置信椭圆通常被认为是覆盖95 % 的置信区间。

    # nstd = 3表示椭圆的长度和宽度分别扩展到3倍标准差的大小，覆盖了大约99.73 % 的数据。这是因为在正态分布中，大约有
    # 99.73 % 的数据落在距离均值三个标准差的范围内。因此，使用nstd = 3绘制置信椭圆通常被认为是覆盖
    # 99 % 的置信区间。但需要注意的是，这里所提到的百分比是基于正态分布的假设。如果数据不符合正态分布，那么覆盖的百分比可能会有所不同。因此，对于非正态分布的数据，确定置信区间的百分比需要使用其他方法。
    # scale95 = math.sqrt(5.991)

    width, height = 3 * 2 * np.sqrt(abs(eigvals))
    # 绘制散点图和置信椭圆
    # fig, ax = plt.subplots()
    ax = plt.gca()
    ax.scatter(x, y, s=1, color=color)
    # 椭圆宽(x)取最大,高(y)取最小,按照逆时针旋转
    # 椭圆宽(x)取最小,高(y)取最大,按照顺时针旋转
    ellipse = Ellipse(xy=mu, width=np.max([width, height]), height=np.min([width, height]), angle=theta,
                      edgecolor=color, fc='None', lw=2, label=str(width) + "," + str(height))
    ax.add_patch(ellipse)
    # 图像属性设置
    ax.set_aspect('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    plt.legend()
    plt.title("Confidence Ellipse")


def mutitG():
    # 均值
    mu0 = np.array([3, 1])
    # 协方差矩阵
    cov0 = np.array([[1, 0.8], [0.8, 1]])
    plotEllipse(mu0, cov0, 'r')

    mu1 = np.array([1, 1])
    # 协方差矩阵
    cov1 = np.array([[0.8, 0.4], [0.4, 0.8]])
    plotEllipse(mu1, cov1, 'g')
    k = np.dot(cov0, np.linalg.inv(cov1 + cov0))
    print("k", k)
    mu = mu0 + np.dot(k, (mu1 - mu0))
    cov = cov0 - np.dot(k, cov0)
    print("mu", mu)
    print("cov", cov)
    plotEllipse(mu, cov, 'y')


if __name__ == "__main__":
    # sigma()
    # test()
    mutitG()
    plt.show()
