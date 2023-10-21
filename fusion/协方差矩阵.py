'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-29 10:41:04
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-09-02 16:12:47
FilePath: /fusion/协方差矩阵.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import transforms3d as tfs


def pell(x, y, mu, sigma):
    # print(sigma)
    # 计算置信椭圆参数
    eigvals, eigvecs = np.linalg.eig(sigma)
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
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=1)
    # 椭圆宽(x)取最大,高(y)取最小,按照逆时针旋转
    # 椭圆宽(x)取最小,高(y)取最大,按照顺时针旋转
    ellipse = Ellipse(xy=mu, width=np.max([width, height]), height=np.min([width, height]), angle=theta,
                      edgecolor='red', fc='None', lw=2)
    ax.add_patch(ellipse)
    # 图像属性设置
    ax.set_aspect('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    plt.title("Confidence Ellipse")

def getSigma(x, y):
    return np.cov([x, y, np.linspace(0, 0, 1000), np.linspace(0, 0, 1000)])


def rotate(trans, mat):
    return np.dot(trans, mat)


def makeTrans(p):
    trans = np.identity(4)
    trans[0:3, 3] = 1
    trans[0:3, 0:3] = tfs.euler.euler2mat(p[0], p[1], math.radians(p[2]), "sxyz")
    return trans


def tuoyuan():
    # 构造数据
    mu = np.array([1, 1])  # 均值
    sigma = np.array([[1, 0.8], [0.8, 1]])  # 协方差矩阵

    x, y = np.random.multivariate_normal(mu, sigma, 1000).T
    trans = makeTrans([0, 0, 45])

    tf = rotate(trans, [x, y, np.linspace(0, 0, 1000), np.linspace(0, 0, 1000)])

    xt = tf[0]
    yt = tf[1]
    # print(yt)

    cov_xy = np.cov([x, y, np.linspace(0, 0, 1000), np.linspace(0, 0, 1000)])
    # print(cov_xy[0:2,0:2])
    newCov = np.dot(np.dot(trans, cov_xy), trans.transpose())
    # print(newCov[0:2,0:2])
    cov_xyt = np.cov(xt, yt)
    print(cov_xy[0:2, 0:2])
    pell(x, y, [np.mean(x), np.mean(y)], cov_xy[0:2, 0:2])
    pell(xt, yt, [np.mean(xt), np.mean(yt)], newCov[0:2, 0:2])
    plt.show()


if __name__ == "__main__":
    tuoyuan()
    # 生成一个4*4的全0矩阵
    # a = np.zeros((4,4))
    # 将矩阵左上方元素赋值为2*2
    # a[0:2,0:2] = np.identity(2)
    # print(a)
