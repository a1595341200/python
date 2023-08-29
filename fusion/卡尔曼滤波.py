'''
Author: yao.xie 1595341200@qq.com
Date: 2023-07-11 12:41:52
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-07-11 15:49:08
FilePath: /python/卡尔曼滤波.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8

import numpy
import pandas
import matplotlib.pyplot
l = 100
dt = 0.025

A = numpy.array([[1,0,dt,0],[0,1,0,dt],[0,0,1,0],[0,0,0,1]])

Q = numpy.eye(4, M =  4, k =  0, dtype =  float)

R = numpy.eye(4, M =  4, k =  0, dtype =  float)

# R = numpy.diag([0.1,0.1,0.1,0.1])

H = numpy.eye(4, M =  4, k =  0, dtype =  float)
print(H)

# print(A)
# print(Q)
# print(R)

w = numpy.random.uniform(-1,1,(l,))
x = numpy.linspace(1,100,l) + w
y = numpy.linspace(1,100,l)
x[50] = 55
# print(x)
df = pandas.DataFrame(y,x)
df.to_csv("test.csv")
df = pandas.DataFrame(numpy.linspace(1,100,l),y)
df.to_csv("real.csv")
# matplotlib.pyplot.scatter(x,y)
# matplotlib.pyplot.show()

# xp = [numpy.array([0,0,0,0])]
xp = numpy.zeros((4,1), dtype = float)
pp = numpy.diag([1,1,1,1])

def predicted(i):
        global xp,pp
        xp = numpy.dot(A,xp)
        pp = numpy.dot(numpy.dot(A, pp) ,A.T) + Q

def update(i):
        global x,y
        global xp,pp
        y1 = numpy.array([[x[i]],[y[i]],[0],[0]]) - numpy.dot(H,xp)
        s = numpy.dot(numpy.dot(H, pp), H.T) + R
        K = numpy.dot(numpy.dot(pp,H.T), numpy.linalg.inv(s))
        xp = xp + numpy.dot(K, y1)
        pp = numpy.dot((numpy.eye(4, M =  4, k =  0, dtype =  float) - numpy.dot(K,H)),pp)

if __name__ == '__main__':
    xtemp = [0]
    ytemp = [0]
    for i in range(1,l):
        predicted(i)
        update(i)
        xtemp.append(xp[0][0])
        ytemp.append(xp[1][0])
        dt += 0.025
    print(len(ytemp))
    # print(xtemp)
    # print(ytemp)
    matplotlib.pyplot.plot(xtemp,ytemp)
    matplotlib.pyplot.plot(numpy.linspace(1,100,l),y)
    matplotlib.pyplot.scatter(x,y)
    matplotlib.pyplot.show()
        
