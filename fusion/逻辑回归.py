'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-28 16:39:15
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-28 16:39:18
FilePath: /fusion/逻辑回归.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
 
# 定义逻辑函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
 
# 定义损失函数
def loss_function(X, y, theta):
    m = len(y)
    h = sigmoid(X.dot(theta))
    J = (-1/m) * np.sum(y*np.log(h) + (1-y)*np.log(1-h))
    return J
 
# 定义梯度下降函数
def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros(num_iters)
    for i in range(num_iters):
        h = sigmoid(X.dot(theta))
        theta -= (alpha/m) * X.T.dot(h - y)
        J_history[i] = loss_function(X, y, theta)
    return theta, J_history
 
# 数据准备
X = np.array([[1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6]])  # 输入特征
y = np.array([0, 0, 1, 1])  # 输出标签
 
# 参数初始化
theta = np.zeros(X.shape[1])  # 初始参数向量
 
# 调用梯度下降函数进行参数估计
alpha = 0.01  # 学习率
num_iters = 1000  # 迭代次数
theta_final, J_history = gradient_descent(X, y, theta, alpha, num_iters)
 
# 输出参数估计结果
print("Final theta:", theta_final)
 
# 输出损失函数的变化情况
import matplotlib.pyplot as plt
plt.plot(range(num_iters), J_history)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.show()
