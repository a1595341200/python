'''
Author: 谢瑶 
Date: 2023-10-13 13:33:44
LastEditors: 谢瑶 
LastEditTime: 2023-10-13 15:38:04
FilePath: /python/mf4/mf4read.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# '''
# Author: 谢瑶
# Date: 2023-10-13 13:33:44
# LastEditors: 谢瑶
# LastEditTime: 2023-10-13 15:13:20
# FilePath: /python/mf4/mf4read.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''
# #! /usr/bin/python3.8
# from asammdf import MDF


# def getSignal(filePath, signalName):
#     f = filePath
#     mdf = MDF(f)
#     signal = mdf.get(signalName)
#     data = signal.samples
#     timestamps = signal.timestamps
#     signal.plot()
#     print(data)

# # 获取所有信号


# def getAllSignal(filePath):
#     f = filePath
#     mdf = MDF(f)
#     chn_db = mdf.channels_db
#     # 代码接上
#     df = mdf.to_dataframe()


# if __name__ == "__main__":
#     filepath = "/Users/xieyao/Desktop/work/mylearning/python/mf4/Recorder_2023-10-10_02-48-29.mf4"
#     # getSignal(filepath, "FCW_Bus_HmiDataFromCllsnFwdWarnCtrl.WarnReq")
#     getAllSignal(filepath)
from asammdf import MDF
import pandas as pd

mdf = MDF(
    '/Users/xieyao/Desktop/work/mylearning/python/mf4/Recorder_2023-10-10_02-48-29.mf4')

# mdf.export(fmt='csv', filename='foo.csv',
#            single_time_base=True, overwrite=True)
chn_db = mdf.channels_db
# 代码接上
df = mdf.to_dataframe()
# print(chn_db)
# for i in chn_db:
#     print(i)
# 遍历key
for i in df:
    # 打印key对应的值
    print(df[i])
