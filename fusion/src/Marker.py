#!/usr/bin/env python3.8
# encoding: utf-8

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
from geometry_msgs.msg import Point , Quaternion
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import time
from tf.transformations import quaternion_from_euler

l = 100
pre = 10
dt = 0.025
A = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])
xk = np.array([[0], [0], [1], [1]])


class Kalman:
    Q = np.diag([1, 1, 1, 1])
    R = np.diag([0.1, 0.1, 1, 1])
    H = np.diag([1, 1, 0, 0])
    x_pre = np.array([[0], [0], [1], [1]])
    p_pre = np.diag([0, 0, 0, 0])
    z_measure_mat = np.array([[0], [0], [1], [1]])

    def __init__(self) -> None:
        pass

    def predicted(self):
        self.x_pre = np.dot(A, self.x_pre)
        self.p_pre = np.dot(np.dot(A, self.p_pre), A.T) + self.Q

    def update(self, z_measure):
        self.z_measure_mat[0][0] = z_measure[0]
        self.z_measure_mat[1][0] = z_measure[1]
        y1 = self.z_measure_mat - np.dot(self.H, self.x_pre)
        s = np.dot(np.dot(self.H, self.p_pre), self.H.T) + self.R
        K = np.dot(np.dot(self.p_pre, self.H.T), np.linalg.inv(s))
        self.x_pre = self.x_pre + np.dot(K, y1)
        self.p_pre = np.dot((np.eye(4) - np.dot(K, self.H)), self.p_pre)


rospy.init_node('path_point_demo')  # 初始化节点
mark_pub = rospy.Publisher('path_point', MarkerArray,
                           queue_size=10)  # 用于发布目标点标记


def send_mark(x, y, z, i):
    markerArray = MarkerArray()  # 创建marker对象
    marker = Marker()
    marker.header.frame_id = 'map'  # 以哪一个TF坐标为原点
    marker.id = 0
    marker.type = marker.CUBE  # 一直面向屏幕的字符格式
    marker.action = marker.ADD  # 添加marker
    marker.scale.x = 1  # marker大小
    marker.scale.y = 1  # marker大小
    marker.scale.z = 1  # marker大小，对于字符只有z起作用
    marker.color.a = 1  # 字符透明度
    marker.color.r = 0  # 字符颜色R(红色)通道
    marker.color.g = 0  # 字符颜色G(绿色)通道
    marker.color.b = 1  # 字符颜色B(蓝色)通道
    marker.pose.position.x = x[i]  # 字符位置
    marker.pose.position.y = y[i]  # 字符位置
    marker.pose.position.z = z  # 字符位置
    r = float('nan')

    if i != 0:
        r = math.atan((y[i]-y[i-1])/(x[i]-x[i-1]))
        quat = quaternion_from_euler(0,0,r)
        marker.pose.orientation.z = quat[2]
    if not np.isnan(r) :
        print(r)

    marker.pose.orientation.w = 1
    markerArray.markers.append(marker)
    marker1 = Marker()
    marker1.header.frame_id = 'map'  # 以哪一个TF坐标为原点
    marker1.id = 1
    marker1.type = marker.LINE_STRIP  # 一直面向屏幕的字符格式
    marker1.action = marker.ADD  # 添加marker
    marker1.scale.x = 0.1  # marker大小
    marker1.scale.y = 0.1  # marker大小
    marker1.scale.z = 0.1  # marker大小，对于字符只有z起作用
    marker1.color.a = 1  # 字符透明度
    marker1.color.r = 0  # 字符颜色R(红色)通道
    marker1.color.g = 1  # 字符颜色G(绿色)通道
    marker1.color.b = 0  # 字符颜色B(蓝色)通道
    p = Point()
    p.x = x[i]
    p.y = y[i]
    p.z = z
    dx = np.array([[x[i]],[y[i]],[1],[1]])
    for i in range(pre) :
        B = A
        B[0][2] += 0.025
        B[1][3] += 0.025
        dx = np.dot(B,dx)
    q = Point()
    q.x = dx[0][0]
    q.y = dx[1][0]
    q.z = 0
    marker1.points.append(p)
    marker1.points.append(q)
    marker1.pose.orientation.w = 1
    markerArray.markers.append(marker1)
    mark_pub.publish(markerArray)


if __name__ == '__main__':
    x_real = []
    y_real = []
    x_w = []
    y_w = []
    kalman = Kalman()
    x_kalman = []
    y_kalman = []
    t = [0]
    for i in range(l):
        A[0][2] = dt
        A[1][3] = dt
        xk = np.dot(A, xk)
        x_real.append(xk[0][0])
        y_real.append(xk[1][0])
        w_x = np.random.uniform(0, 0.1, (1,))
        w_y = np.random.uniform(0, 0.1, (1,))
        x_w.append(xk[0][0] + w_x)
        y_w.append(xk[1][0] + w_y)
        kalman.predicted()
        z_measure = [xk[0][0] + w_x, xk[1][0] + w_y]
        kalman.update(z_measure)
        x_kalman.append(kalman.x_pre[0][0])
        y_kalman.append(kalman.x_pre[1][0])
        dt += 0.025
        t.append(dt)
        send_mark(x_kalman, y_kalman, 0, i)
        time.sleep(0.025)
    plt.subplot(1, 2, 1)
    plt.plot(x_real, y_real, color="blue")
    plt.plot(x_kalman, y_kalman, color="green")
    plt.scatter(x_w, y_w, color="red")
    plt.subplot(1, 2, 2)
    plt.plot(t[:l], np.array(x_kalman) - np.array(x_real))
    rems = np.var(np.array(x_kalman) - np.array(x_real))
    rems = math.sqrt(rems)
    print(rems)
    plt.show()
    while not rospy.is_shutdown():
        r = rospy.Rate(100)
        r.sleep()
