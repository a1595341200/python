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
            print("finally------>", l)
