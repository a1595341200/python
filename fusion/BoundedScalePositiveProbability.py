'''
Author: yao.xie 1595341200@qq.com
Date: 2023-09-01 17:12:39
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-09-26 10:03:26
FilePath: /python/fusion/BoundedScalePositiveProbability.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib

a = np.arange(0, 1, 0.01)

def BoundedScalePositiveProbability(p, max_p, min_p) :
  p = max(p, min_p)
  p = (p - min_p) * (max_p - min_p) / (1 - min_p) + min_p
  return p

if __name__ == "__main__":
    matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")
    y = list()
    for i in a :
        y.append(BoundedScalePositiveProbability(i, 0.6, 0.5))
    plt.plot(a, y)
    plt.xlabel('prob')
    plt.ylabel('scale_prob')
    plt.title('BoundedScalePositiveProbability')
    plt.show()
