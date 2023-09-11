'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-30 14:57:07
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-30 15:02:09
FilePath: /python/fusion/scale_probability.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# /usr/bin/python3.8
import numpy as np
import math
import matplotlib.pyplot as plt

a = np.linspace(0,1,10)

def scale_probability(p, max_p, min_p):
    if p > 0.5 :
      p = 0.5 + (p - 0.5) * (max_p - 0.5) / 0.5
    else :
      p = 0.5 - (0.5 - p) * (0.5 - min_p) / 0.5
    return p

if __name__ == '__main__':
    y = list()
    for i in a :
        y.append(scale_probability(i,0.8,0.2))
    plt.plot(a,y)
    plt.show()
