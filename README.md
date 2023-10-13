<!--
 * @Author: 谢瑶 
 * @Date: 2023-08-28 09:29:50
 * @LastEditors: 谢瑶 
 * @LastEditTime: 2023-10-13 16:22:47
 * @FilePath: /python/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
- [1. python](#1-python)
  - [1.1. numpy](#11-numpy)
    - [1.1.1. ogrid](#111-ogrid)
    - [1.1.2. NumPy教程-numpy.mean()在Python中的使用](#112-numpy教程-numpymean在python中的使用)
      - [1.1.2.1. 语法](#1121-语法)

# 1. python
## 1.1. numpy
### 1.1.1. ogrid
&emsp;&emsp;ogrid函数官网介绍

&emsp;&emsp;ogrid函数作为产生numpy数组与numpy的arange函数功能有点类似，不同的是：

&emsp;&emsp;1. arange函数产生的是一维数组，而ogrid函数产生的是二维数组

&emsp;&emsp;2. arange函数产生的是一个数组，而ogrid函数产生的是二个数组

&emsp;&emsp;3. ogrid函数产生的数组，第一个数组是以纵向产生的，即数组第二维的大小始终为1。第二个数组是以横向产生的，即数组第一维的大小始终为1。

&emsp;&emsp;下面详细介绍ogrid函数的两种用法：
&emsp;&emsp;1. 整数步长
第一个数组的步长为1，第二数组的步长为2
```
    x,y = np.ogrid[0:10:1,0:10:2]
    print(x,np.shape(x))
    print(y,np.shape(y))
```
&emsp;&emsp;2. 复数步长
复数步长的设置是通过j进行设置的，如5j。复数前表示的是，用几个数值来等分整个区间。
```
    x,y = np.ogrid[0:10:6j,0:10:4j]
    print(x,np.shape(x))
    print(y,np.shape(y))
```
### 1.1.2. NumPy教程-numpy.mean()在Python中的使用

### 1.1.3. NumPy教程-numpy.transpose()在Python中的使用
