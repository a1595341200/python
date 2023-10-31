<!--
 * @Author: 谢瑶 
 * @Date: 2023-08-28 09:29:50
 * @LastEditors: 谢瑶 
 * @LastEditTime: 2023-10-31 14:03:58
 * @FilePath: /python/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
- [1. python](#1-python)
  - [1.1. numpy](#11-numpy)
    - [1.1.1. ogrid](#111-ogrid)
    - [1.1.2. NumPy教程-numpy.mean()在Python中的使用](#112-numpy教程-numpymean在python中的使用)
    - [1.1.3. NumPy教程-numpy.transpose()在Python中的使用](#113-numpy教程-numpytranspose在python中的使用)
  - [1.2. 卡尔曼滤波](#12-卡尔曼滤波)
    - [1.2.1. 高斯公式](#121-高斯公式)
    - [1.2.2. 高斯相乘](#122-高斯相乘)
    - [1.2.3. 把它们结合在一起](#123-把它们结合在一起)
  - [1.3. UKF](#13-ukf)

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
## 1.2. 卡尔曼滤波
https://zhuanlan.zhihu.com/p/39912633
https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
### 1.2.1. 高斯公式
![高斯公式](https://pic1.zhimg.com/80/v2-97fd17b2ea76d5452a22725f19f99580_1440w.webp)
### 1.2.2. 高斯相乘

&emsp;&emsp;![高斯公式](https://pic2.zhimg.com/80/v2-95a639e3feb8773757a4a74e45e477c5_1440w.webp)

&emsp;&emsp;![高斯公式](https://pic2.zhimg.com/80/v2-44fae648700cd28c6ed7c82e91c864a9_1440w.webp)

&emsp;&emsp;把这个式子按照一维方程进行扩展，可得：

&emsp;&emsp;![高斯公式](https://pic2.zhimg.com/80/v2-f3119ec5da2279746e27b0e2e31ccfb9_1440w.webp)

&emsp;&emsp;如果有些太复杂，我们用k简化一下：

&emsp;&emsp;![高斯公式](https://pic2.zhimg.com/80/v2-2881114c10fc274482b013e408df9ce9_1440w.webp)

&emsp;&emsp;以上是一维的内容，如果是多维空间，把这个式子转成矩阵格式：

&emsp;&emsp;![高斯公式](https://pic1.zhimg.com/80/v2-1c02a4b31a146aba44c5082079df1e8c_1440w.webp)
这个矩阵$K$就是我们说的卡尔曼增益，easy！

### 1.2.3. 把它们结合在一起
&emsp;&emsp;截至目前，我们有用矩阵预测的分布$(\mu_0,\Sigma_0) = (H_k\hat{x}_k,H_kP_kH^T_k)$, 有用传感器读数$(\mu_1,\Sigma_1)=(\vec{z},R_k)$预测的分布。把它们代入上节的矩阵等式中：

&emsp;&emsp;![高斯公式](https://pic4.zhimg.com/80/v2-9cb02f4cb340f4bee98bf8fdef80867b_1440w.webp)

&emsp;&emsp;相应的，卡尔曼增益就是：

&emsp;&emsp;![高斯公式](https://pic2.zhimg.com/80/v2-c2a3f0e191354e598e09d4fdd59b8d25_1440w.webp)

&emsp;&emsp;考虑到$K$里还包含着一个$H_k$，我们再精简一下上式

&emsp;&emsp;![高斯公式](https://pic3.zhimg.com/80/v2-47b92e3442751ff8266b4d18e30bda2a_1440w.webp)

&emsp;&emsp;最后, $\hat{x}{^,}_k$是我们的最佳估计值，我们可以把它继续放进去做另一轮预测：

&emsp;&emsp;![高斯公式](https://pic3.zhimg.com/80/v2-c4db49174bd28fa7634be3858a368e26_1440w.webp)
## 1.3. UKF
https://www.cnblogs.com/21207-iHome/p/5235768.html
