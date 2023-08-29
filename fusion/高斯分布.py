'''
Author: yao.xie 1595341200@qq.com
Date: 2023-07-11 12:35:06
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-07-11 12:35:21
FilePath: /python/高斯分布.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8

# plot Gaussian Function
# 注：正态分布也叫高斯分布
import matplotlib.pyplot as plt
import numpy as np
 
u1 = 0  # 第一个高斯分布的均值
sigma1 = 1  # 第一个高斯分布的标准差
 
u2 = 1  # 第二个高斯分布的均值
sigma2 = 2  # 第二个高斯分布的标准差
x = np.arange(-5, 5, 0.1)
# 表示第一个高斯分布函数
y1 = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma1, -1), np.exp(-np.power(x - u1, 2) / 2 * sigma1 ** 2))
# 表示第二个高斯分布函数
y2 = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma2, -1), np.exp(-np.power(x - u2, 2) / 2 * sigma2 ** 2))
 
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决pythonmatplotlib绘图无法显示中文的问题
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
 
plt.subplot(121)
plt.plot(x, y1, 'b-', linewidth=2)
plt.title("高斯分布函数图像")
 
plt.subplot(122)
plt.plot(x, y2, 'r-', linewidth=2)
plt.title('高斯分布函数图像')
plt.show()
