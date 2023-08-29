'''
Author: yao.xie 1595341200@qq.com
Date: 2023-07-11 12:41:52
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-07-12 16:26:05
FilePath: /python/卡尔曼滤波.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
l = 40
dt = 0
A = np.array([[1.0, 0, dt, 0], [0, 1.0, 0, dt], [
             0, 0, 1.0, 0], [0, 0, 0, 1.0]], dtype=float)
xk = np.array([[0.0], [0.0], [0.0], [0.0]], dtype=float)


class Kalman:
    Q = np.diag([0.1, 0.1, 1.0, 1.0])
    R = np.diag([1.0, 1.0, 1.0, 1.0])
    H = np.diag([1.0, 1.0, 0.0, 0.0])
    x_pre = np.array([[0.0], [0.0], [0.0], [0.0]], dtype=float)
    p_pre = np.diag([0.0, 0.0, 0.0, 0.0])
    z_measure_mat = np.array([[0.0], [0.0], [1.0], [1.0]], dtype=float)

    def __init__(self) -> None:
        pass

    def predicted(self):
        self.x_pre = np.dot(A, self.x_pre)
        self.p_pre = np.dot(np.dot(A, self.p_pre), A.T) + self.Q

    def update(self, z_measure):
        self.z_measure_mat[0][0] = z_measure[0]
        self.z_measure_mat[1][0] = z_measure[1]
        y1 = self.z_measure_mat - np.dot(self.H, self.x_pre)
        print(y1)
        s = np.dot(np.dot(self.H, self.p_pre), self.H.T) + self.R
        K = np.dot(np.dot(self.p_pre, self.H.T), np.linalg.inv(s))
        self.x_pre = self.x_pre + np.dot(K, y1)
        self.p_pre = np.dot((np.eye(4) - np.dot(K, self.H)), self.p_pre)


if __name__ == '__main__':
    x_real = []
    y_real = []
    x_w = []
    y_w = []
    kalman = Kalman()
    x_kalman = []
    y_kalman = []
    t = []
    for i in range(l):
        A[0][2] = dt
        A[1][3] = dt
        # xk = np.dot(A, xk)
        xk[0][0] += 0.025
        xk[1][0] += 0.025
        # print(xk)
        x_real.append(dt)
        y_real.append(dt)
        w_x = np.random.uniform(-0.03, 0.03, (1,))
        w_y = np.random.uniform(-0.03, 0.03, (1,))
        x_w.append(dt + w_x)
        y_w.append(dt + w_y)
        kalman.predicted()
        z_measure = [dt + w_x, dt + w_y]
        kalman.update(z_measure)
        x_kalman.append(kalman.x_pre[0][0])
        y_kalman.append(kalman.x_pre[1][0])
        dt += 0.025
        t.append(dt)
    plt.subplot(1, 2, 1)
    plt.plot(x_real, y_real, color="blue")
    plt.plot(x_kalman, y_kalman, color="green")
    plt.scatter(x_w, y_w, color="red")
    plt.subplot(1, 2, 2)
    plt.plot(t[:l], np.array(x_kalman) - np.array(x_real))
    # plt.plot(t[:l], x_kalman)
    rems = np.var(np.array(x_kalman) - np.array(x_real))
    rems = math.sqrt(rems)
    print(rems)
    plt.show()
