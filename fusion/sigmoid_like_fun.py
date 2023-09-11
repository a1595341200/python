'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-28 13:32:18
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-30 13:59:19
FilePath: /fusion/威尔逊损失函数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8

import numpy as np
import math
import matplotlib.pyplot as plt

a = np.array(np.linspace(0, 110, 10000))

def sigmoid_like_fun(max_dist, dist_slope, obj_dist) :
    x = obj_dist - max_dist
    return 0.5 - 0.5 * x * dist_slope /  math.sqrt(1 + x * x * dist_slope * dist_slope)


def testDist_slope(dist_slope) :
    y = list()
    for i in range(len(a)) :    
        y.append(sigmoid_like_fun(110,dist_slope, a[i]))
    return y

if __name__ == '__main__':
    
    for i in [0.25,0.5,1,10,100] :
        plt.plot(a, testDist_slope(i), label = str(i))
  
    plt.legend()
    plt.show()
