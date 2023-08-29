'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-28 13:32:18
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-28 17:50:42
FilePath: /fusion/威尔逊损失函数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8

import numpy as np
import math
import matplotlib.pyplot as plt

a = np.array(np.linspace(0, 3, 100))
a1 = np.array(np.linspace(1e-6, 1, 100))
def ScalePositiveProbability(max_p_) :
    y = (a1 - 0.5) * (max_p_ - 0.5) / (1 - 0.5) + 0.5
    return y

plt.figure()
# 显示刻度
# plt.xticks() 
def WelshVarLossFun(sc):
    temp = np.array(a)
    for i in range(len(a)) :
        if(temp[i] < 0.5) :
            temp[i] = 1
        else :
            temp[i] -= 0.5
            temp[i] /= sc
            temp[i] = math.exp(-temp[i]*temp[i])
    return temp

def prob_to_log_odd(p):
    p = max(min(p, 1 - 1e-6), 1e-6)
    return math.log(p / (1 - p))

def log_odd_to_prob(log_odd_p):
    tmp = math.exp(log_odd_p)
    return tmp / (tmp + 1)

# Logistic回归 二分类回归模型
def FuseMultipleProbabilities(probs) :
  log_odd_probs = probs

  for log_odd_prob in log_odd_probs :
    log_odd_prob = prob_to_log_odd(log_odd_prob)
  log_odd_probs_sum = 0

  for i in range(len(log_odd_probs)) :
      log_odd_probs_sum += log_odd_probs[i]
  
  print(log_odd_probs_sum)
  return log_odd_to_prob(log_odd_probs_sum)

def FuseTwoProbabilities(prob1, prob2) :
    prob = (prob1 * prob2) / (2 * prob1 * prob2 + 1 - prob1 - prob2)
    return prob

def test() :
    plt.subplot(121)
    for x in [0.3,0.4,0.5,0.6,0.7,0.8] :
        plt.plot(a, WelshVarLossFun(x),label = str(x))
    plt.legend(loc = 'best')
    plt.plot([0.5,0.5],[1,0])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # ax.spines['left'].set_position(('axes', 0))
    plt.subplot(122)
    for x in [0.9,0.8,0.7,0.6,0.5,0.4] :
        plt.plot(a1,ScalePositiveProbability(x),label = str(x))
    plt.plot([0.5,0],[0.5,0.5],color = 'b')
    plt.plot([0.5,0.5],[0.5,0],color = 'b')
    plt.legend(loc = 'best')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # ax.annotate('0.5', xy=(0.5, 0.5), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05))
    # bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
    '''
        以文本坐标(-2,-2)
        ha="center"  在水平方向上，方框的中心在为（-2,0)
        va="center"  在垂直方向上，方框的中心在为(0,-2)
        size = '20' 代表方框的大小
        bbox={}  代表对方框的设置
            { 
                boxstyle= '' 代表边框的类型
                        round 圆形方框
                        rarrow箭头
                fc  背景颜色   英文首字母 w -whiite r-red
                ec 边框线的透明度  数字或颜色的首字母
                alpha 字体的透明度
                lw 线的粗细
                rotation  角度
            }
    '''
    # ax.text(0.5, 0.5, "Sample A", ha="center", va="center", size=5, bbox=bbox_props)
    plt.show()

def testFuseMultipleProbabilities() :
    probs = [0.1,0.5,0.3,0.8]
    # probs = [0.01]
    return FuseMultipleProbabilities(probs)

def testTrans() :
    y = list()
    for i in a1:
        y.append(math.log(i/(1 - i)))
        
    plt.plot(a1,y)
    plt.show()

if __name__ == '__main__':
    print(testFuseMultipleProbabilities())
    testTrans()
    