'''
Author: 谢瑶 
Date: 2023-10-13 13:33:44
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2023-10-26 10:51:24
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
import matplotlib.pyplot as plt


def test1() :
    mdf = MDF(
    '/home/user/work/mylearning/python/mf4/Recorder_2023-10-10_02-48-29.mf4')

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

def getsignal(name, mdf):
    signal = mdf.get(name)
    data = signal.samples
    timestamps = signal.timestamps
    return timestamps, data

def AEBTimeIndex(mdf):
    timestamps,data = getsignal('CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.DecelReq',mdf)
    res = -1
    for i in range(len(data)):
        if data[i] > 0:
            res = i
            break
    return res

def test() :
    f = r"/home/user/work/mylearning/python/mf4/Recorder_2023-10-10_02-48-29.mf4"
    mdf = MDF(f)
    timestamps,data = getsignal('CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.CllsnThreat',mdf)
    plt.subplot(2,2,1)
    plt.plot(timestamps, data, label='CllsnThreat')
    plt.legend()
    plt.subplot(2,2,2)
    timestamps,data = getsignal('CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.DecelReq',mdf)
    plt.plot(timestamps, data,label='DecelReq')
    plt.legend()
    plt.subplot(2,2,3)
    timestamps,data = getsignal('CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.Idn',mdf)
    plt.plot(timestamps, data,label='Idn')
    plt.legend()
    plt.subplot(2,2,4)
    timestamps, posnLgtdata = getsignal('CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.PosnLgt',mdf)
    timestamps, posnLatdata = getsignal('CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.PosnLat',mdf)

    index = AEBTimeIndex(mdf)
    print(index)
    plt.scatter([0,posnLatdata[index]], [0,posnLgtdata[index]],label='Posn')
    plt.xlim(-posnLatdata[index]-1, posnLatdata[index]+1)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test()
