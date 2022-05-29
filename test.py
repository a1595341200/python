#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
print( "你好，世界" )

import os
import sys
logf = open("log.txt", "a+")
logf.seek(0)
print(logf.read())
logf.seek(os.SEEK_END)
print("Hello World")
logf.close()
if __name__ == '__main__':
    print("main")
