'''
Author: yao.xie 1595341200@qq.com
Date: 2023-08-31 14:19:26
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-08-31 14:32:54
FilePath: /python/fusion/BBOX2D.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#/usr/bin/python3.8
class BBox2D :
    def __init__(self, xmin,xmax,ymin, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        
    @classmethod
    def empty(cls):
        return cls(0,0,0,0)

    def Center(self) :
        return [self.xmin + (self.xmax - self.xmin) / 2, self.ymin + (self.ymax - self.ymin) / 2]

    def Area(self): 
        return (self.xmax - self.xmin) * (self.ymax - self.ymin)
    
if __name__ == "__main__":
    a = BBox2D(0,100,0,100)
    print(a.Center())
    print(a.Area())
