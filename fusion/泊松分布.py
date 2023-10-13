'''
Author: 谢瑶 
Date: 2023-10-12 16:24:45
LastEditors: 谢瑶 
LastEditTime: 2023-10-12 16:25:11
FilePath: /python/fusion/泊松分布.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

X = range(0, 51)
Y = []
for k in X:
    p = stats.poisson.pmf(k, 20)
    Y.append(p)

plt.bar(X, Y, color="red")
plt.xlabel("次数")
plt.ylabel("概率")
plt.title("接到骚扰电话次数及概率")
plt.show()
