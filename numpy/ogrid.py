'''
Author: 谢瑶 
Date: 2023-10-10 11:28:26
LastEditors: 谢瑶 
LastEditTime: 2023-10-10 11:32:36
FilePath: /python/numpy/ogrid.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

x, y = np.ogrid[0:10:1, 0:10:2]
print(x, np.shape(x))
print(y, np.shape(y))
