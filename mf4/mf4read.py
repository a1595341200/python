'''
Author: 谢瑶 
Date: 2023-10-13 13:33:44
LastEditors: 谢瑶 
LastEditTime: 2023-10-27 12:59:35
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


import os

import matplotlib.pyplot as plt
# if __name__ == "__main__":
#     filepath = "/Users/xieyao/Desktop/work/mylearning/python/mf4/Recorder_2023-10-10_02-48-29.mf4"
#     # getSignal(filepath, "FCW_Bus_HmiDataFromCllsnFwdWarnCtrl.WarnReq")
#     getAllSignal(filepath)
from asammdf import MDF

path = '/Users/xieyao/Desktop/work/mylearning/python/mf4/Recorder_2023-10-27_09-57-37.mf4'


def test1():
    mdf = MDF(path)

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
    flag = False
    timestamps, data = getsignal('CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.DecelReq', mdf)
    res = []
    for i in range(len(data)):
        if data[i] > 0 and flag == False:
            res.append(i)
            flag = True
        if data[i] <= 0 and flag == True:
            flag = False
    return res


def getAEBorFCW100Frame(timestamps, data, index):
    begin = index - 100
    end = index + 100
    return timestamps[begin:end], data[begin:end]


def subplot(row, col, cur, signalName, mdf, index):
    timestamps, data = getsignal(signalName, mdf)
    plt.subplot(row, col, cur)
    timestamps, data = getAEBorFCW100Frame(timestamps, data,index)
    plt.plot(timestamps, data, label=os.path.basename(signalName).split('.')[-1])
    plt.legend()


def test():
    mdf = MDF(path)
    index = AEBTimeIndex(mdf)
    row = 4
    col = 4
    for i in index:
        print("i = ",i)
        fig = plt.figure()
        subplot(row, col, 1, 'CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.CllsnThreat', mdf,i)
        subplot(row, col, 2, 'CMBB_Bus_ActtnDataFromCllsnRednByBrkgCtrl.DecelReq', mdf,i)
        subplot(row, col, 3, 'CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.Idn', mdf,i)

        plt.subplot(row, col, 4)
        timestamps, posnLgtdata = getsignal('CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.PosnLgt', mdf)
        timestamps, posnLatdata = getsignal('CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.PosnLat', mdf)
        timestamps, posnLgtdata = getAEBorFCW100Frame(timestamps, posnLgtdata,i)
        timestamps, posnLatdata = getAEBorFCW100Frame(timestamps, posnLatdata,i)
        plt.scatter(posnLatdata, posnLgtdata, label='Pose')
        plt.scatter(0, 0, label='ego')

        plt.xlim(-posnLatdata[0] - 1, posnLatdata[len(posnLatdata)-1] + 1)
        plt.legend()

        subplot(row, col, 5, 'CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.ALat', mdf,i)
        subplot(row, col, 6, 'CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.ALgt', mdf,i)
        subplot(row, col, 7, 'CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.ObjTyp', mdf,i)
        subplot(row, col, 8, 'CLTS_Bus_CritLgtCdnForIntv_CritLgtCdnForIntv0.PrimTarIntv.MtnPat', mdf,i)
        subplot(row, col, 9, 'ISM_Bus_EgoMotionData_EgoMotion.Speed', mdf,i)
        subplot(row, col, 10, 'ISM_Bus_EgoMotionData_EgoMotion.ALgt', mdf,i)
        subplot(row, col, 11, 'ISM_Bus_EgoMotionData_EgoMotion.ALat', mdf,i)
        subplot(row, col, 12, 'ISM_Bus_EgoMotionData_EgoMotion.YawRate', mdf,i)

        plt.show()
    plt.show()


if __name__ == "__main__":
    test()
