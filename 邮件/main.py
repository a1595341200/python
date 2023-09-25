#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__(self, sender='1595341200@qq.com', pw='ohupmuldobufhgda', user='1595341200@qq.com'):
        self.server = None
        self.message = MIMEMultipart()
        self.sender = sender  # 发件人邮箱账号
        self.pw = pw  # 发件人邮箱密码
        self.user = user  # 收件人邮箱账号，我这边发送给自己
        self.login()
        self.make_title()

    def send(self):
        self.send_email(self.message)

    def attach_file(self, filename = "test", path = ''):
        try:
            # 构造附件1，传送当前目录下的 test.txt 文件
            # att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
            att1 = MIMEText("dfsdf", 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename=' + filename
            self.message.attach(att1)
        except Exception:
            print("添加附件失败")

    def make_title(self, line="内容\n"):
        msg = MIMEText(line, 'plain', 'utf-8')
        self.message['From'] = formataddr(["yao.xie", self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        self.message['To'] = formataddr(["test", self.user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        self.message['Subject'] = "谢瑶发送邮件测试"  # 邮件的主题，也可以说是标题
        self.message.attach(msg)

    def send_email(self, message):
        try:
            self.server.sendmail(self.sender, [self.user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            print("发送成功")
        except Exception:
            print("发送失败")

    def login(self):
        try:
            self.server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            self.server.login(self.sender, self.pw)  # 括号中对应的是发件人邮箱账号、邮箱密码
            print("login success")
        except Exception:
            print("login failed !")


if __name__ == "__main__":
    # e = Email()
    # e.attach_file()
    # e.send()
    p = float(random.randint(1,600))
    time.sleep(p)

