# ogrid
ogrid函数官网介绍

ogrid函数作为产生numpy数组与numpy的arange函数功能有点类似，不同的是：

1、arange函数产生的是一维数组，而ogrid函数产生的是二维数组

2、arange函数产生的是一个数组，而ogrid函数产生的是二个数组

3、ogrid函数产生的数组，第一个数组是以纵向产生的，即数组第二维的大小始终为1。第二个数组是以横向产生的，即数组第一维的大小始终为1。

下面详细介绍ogrid函数的两种用法：
1、整数步长
第一个数组的步长为1，第二数组的步长为2
```
    x,y = np.ogrid[0:10:1,0:10:2]
    print(x,np.shape(x))
    print(y,np.shape(y))
```
2、复数步长
复数步长的设置是通过j进行设置的，如5j。复数前表示的是，用几个数值来等分整个区间。
```
    x,y = np.ogrid[0:10:6j,0:10:4j]
    print(x,np.shape(x))
    print(y,np.shape(y))
```
