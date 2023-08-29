'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-29 10:41:04
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-29 11:18:58
FilePath: /fusion/协方差矩阵.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

if __name__ == "__main__":
    # 构造数据
    mu = np.array([0, 0])  # 均值
    sigma = np.array([[1, 0.8], [0.8, 1]])  # 协方差矩阵
    print(sigma)
    x, y = np.random.multivariate_normal(mu, sigma, 1000).T
    # 计算置信椭圆参数
    eigvals, eigvecs = np.linalg.eig(sigma)
    theta = -np.degrees(np.arctan2(*eigvecs[0]))
    print(eigvals)
    width, height = 2 * np.sqrt(abs(eigvals))
    # 绘制散点图和置信椭圆
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=1)
    ellipse = Ellipse(xy=mu, width=width, height=height, angle=theta,
                      edgecolor='red', fc='None', lw=2)
    ax.add_patch(ellipse)
    # 图像属性设置
    ax.set_aspect('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    plt.title("Confidence Ellipse")
    plt.show()
