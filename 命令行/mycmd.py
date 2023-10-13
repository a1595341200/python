'''
Author: 谢瑶 
Date: 2022-09-29 11:58:13
LastEditors: 谢瑶 
LastEditTime: 2023-10-13 15:57:49
FilePath: /python/命令行/mycmd.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import subprocess


class Cmd:
    def __init__(self, cmd):
        self.cmd = cmd

    def start(self):
        if (self.cmd == None):
            print("cmd为空")
        else:
            ret = subprocess.Popen(self.cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            l = []
            for i in iter(ret.stdout.readline, b""):
                print(i.decode().strip())
                l.append(i.decode().strip())
            # print("finally------>", l)
            print(self.cmd, " 执行完毕")
