'''
Author: yao.xie 1595341200@qq.com
Date: 2023-07-11 12:35:06
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2024-03-21 09:50:27
FilePath: /python/fusion/单调性.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8

# plot Gaussian Function
# 注：正态分布也叫高斯分布
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Ellipse

def test():
    x = np.arange(0.1, 10, 0.1)
    y = x / (x + 1)
    plt.plot(x,y)
    pass

if __name__ == "__main__":
    test()
    plt.show()
