'''
Author: 谢瑶 
Date: 2023-10-31 14:07:31
LastEditors: 谢瑶 
LastEditTime: 2023-10-31 14:21:54
FilePath: /python/fusion/UFK对比.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np
from filterpy.kalman import MerweScaledSigmaPoints as SigmaPoints
from filterpy.kalman import unscented_transform
from numpy.random import multivariate_normal
from scipy import stats


# 非线性变换函数
def f_nonlinear_xy(x, y):
    return np.array([x + y, 0.1 * x ** 2 + y ** 2])


def plot1(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    xmin = xs.min()
    xmax = xs.max()
    ymin = ys.min()
    ymax = ys.max()
    values = np.vstack([xs, ys])
    kernel = stats.gaussian_kde(values)
    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    Z = np.reshape(kernel.evaluate(positions).T, X.shape)
    plt.imshow(np.rot90(Z), cmap=plt.cm.Greys, extent=[xmin, xmax, ymin, ymax])
    plt.plot(xs, ys, 'k.', markersize=2)
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)


def plot2(xs, ys, f, mean_fx):
    fxs, fys = f(xs, ys)  # 将采样点进行非线性变换
    computed_mean_x = np.average(fxs)
    computed_mean_y = np.average(fys)
    plt.subplot(121)
    plt.grid(False)
    plot1(xs, ys)
    plt.subplot(122)
    plt.grid(False)
    plot1(fxs, fys)
    plt.scatter(fxs, fys, marker='.', alpha=0.01, color='k')
    plt.scatter(mean_fx[0], mean_fx[1], marker='o', s=100, c='r', label='UT_mean')
    plt.scatter(computed_mean_x, computed_mean_y, marker='*', s=120, c='b', label='mean')
    plt.ylim([-10, 200])
    plt.xlim([-100, 100])
    plt.legend(loc='best', scatterpoints=1)
    print('Difference in mean x={:.3f}, y={:.3f}'.format(
        computed_mean_x - mean_fx[0], computed_mean_y - mean_fx[1]))


# -------------------------------------------------------------------------------------------
mean = [0, 0]  # Mean of the N-dimensional distribution.
cov = [[32, 15], [15, 40]]  # Covariance matrix of the distribution.

# create sigma points(2n+1个sigma点)
# uses 3 parameters to control how the sigma points are distributed and weighted
points = SigmaPoints(n=2, alpha=.1, beta=2., kappa=1.)
# Wm, Wc = points.weights
Wm = points.Wm
Wc = points.Wc
sigmas = points.sigma_points(mean, cov)

# pass through nonlinear function
sigmas_f = np.empty((5, 2))
for i in range(5):
    sigmas_f[i] = f_nonlinear_xy(sigmas[i, 0], sigmas[i, 1])

# use unscented transform to get new mean and covariance
ukf_mean, ukf_cov = unscented_transform(sigmas_f, Wm, Wc)

# generate random points
xs, ys = multivariate_normal(mean, cov, size=1000).T  # 从二维随机变量的正态分布中产生1000个数据点
plot2(xs, ys, f_nonlinear_xy, ukf_mean)

# 画sigma点
plt.xlim(-30, 30);
plt.ylim(0, 90)
plt.subplot(121)
plt.scatter(sigmas[:, 0], sigmas[:, 1], c='r', s=30)
plt.show()
