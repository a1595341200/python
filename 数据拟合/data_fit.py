'''
Author: yao.xie yao.xie@jicaai.com
Date: 2023-11-28 10:51:24
LastEditors: yao.xie yao.xie@jicaai.com
LastEditTime: 2023-11-28 13:24:33
FilePath: /python/数据拟合/数据拟合.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import numpy
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

threshold = 0.30
distance_threshold = 60


def Pfun(t, BETA_0, BETA_1, BETA_2, BETA_3, BETA_4, BETA_5):
    return BETA_0 + BETA_1 * abs(t[1]) + BETA_2 * abs(t[0]) + BETA_3 * np.power(t[1], 2) + BETA_4 * np.power(t[0],
                                                                                                             2) + BETA_5 * \
        abs(t[0] * t[1])


class Fit:
    def __init__(self):
        self.__map = {"gt_lat_dis": [], "gt_lgt_dis": [], "error_lat": [],
                      "error_lgt": []}

        self.__mes_lat = []
        self.__mes_lgt = []
        self.res_x = []
        self.res_y = []
        self.__reader = []

    def __getInternalDate(self):
        row = 0
        rel_row = 0
        for index, val in self.__reader.iterrows():
            ratiox = abs(val["error_lat"] / val["gt_lat_dis"])
            ratioy = abs(val["error_lgt"] / val["gt_lgt_dis"])
            if abs(val["gt_lat_dis"]) < distance_threshold and abs(val["gt_lgt_dis"]) < distance_threshold:
                row += 1

            if abs(val["gt_lat_dis"]) < distance_threshold and abs(val["gt_lgt_dis"]) < distance_threshold and abs(
                    val["error_lat"]) < 10 and abs(
                val["error_lgt"]) < 10 and ratiox < threshold and ratioy < threshold:
                self.__map['gt_lat_dis'].append(val["gt_lat_dis"])
                self.__map['gt_lgt_dis'].append(val["gt_lgt_dis"])
                self.__map['error_lat'].append(val["error_lat"])
                self.__map['error_lgt'].append(val["error_lgt"])
                rel_row += 1
            else:
                # print("error ", val[1])
                # print("ratiox ", ratiox)
                # print("ratioy ", ratioy)
                pass
        print("row", row)
        print("rel_row", rel_row)
        print("比率", rel_row / row)

    def __getData(self, name):
        self.__reader = pd.read_csv(name, usecols=[3, 4, 5, 6])
        self.__getInternalDate()

        self.__mes_lat = np.array(self.__map['gt_lat_dis']) + np.array(self.__map['error_lat'])
        self.__mes_lgt = np.array(self.__map['gt_lgt_dis']) + np.array(self.__map['error_lgt'])

        return self.__map['gt_lat_dis'], self.__map['gt_lgt_dis'], self.__map['error_lat'], self.__map[
            'error_lgt'], self.__mes_lat, self.__mes_lgt

    def doFit(self, path, name):
        self.__map['gt_lat_dis'] = []
        self.__map['gt_lgt_dis'] = []
        self.__map['error_lat'] = []
        self.__map['error_lgt'] = []
        self.__mes_lat = []
        self.__mes_lat = []
        self.__reader = []

        self.__getData(path)

        xy0 = np.vstack([self.__mes_lat, self.__mes_lgt])
        return self.__curveFit(name, Pfun, xy0, self.__map['error_lgt'], self.__map['error_lat'])

    def __curveFit(self, name, Pfun, xy0, error_lgt, error_lat):
        print(name)
        self.res_x, cov_x = curve_fit(Pfun, xy0, error_lgt)
        self.res_y, cov_y = curve_fit(Pfun, xy0, error_lat)
        print("lgt\n", self.res_x)
        # print("cov_x\n", cov_x)
        print("lat\n", self.res_y)
        # print("cov_y\n", cov_y)
        return self.res_x, cov_x, self.res_y, cov_y

    def test(self):

        for index, val in self.__reader.iterrows():
            ratiox = abs(val['error_lat'] / val['gt_lat_dis'])
            ratioy = abs(val['error_lgt'] / val['gt_lgt_dis'])
            if abs(val["gt_lat_dis"]) < 10 and val["gt_lgt_dis"] < distance_threshold and abs(
                    val["error_lat"]) < 10 and abs(
                val["error_lgt"]) < 10 and ratiox < threshold and ratioy < threshold:
                m_y = val["gt_lat_dis"] + val["error_lat"]
                m_x = val["gt_lgt_dis"] + val["error_lgt"]
                # print('lat', val["gt_lat_dis"])
                # print('lgt', val["gt_lgt_dis"])
                # print('error_lgt', val["error_lgt"])
                # print('error_lat', val["error_lat"])
                position_x = m_x
                position_y = m_y
                f32PosVarX = self.res_x[0]
                f32PosVarX += self.res_x[1] * abs(position_x)
                f32PosVarX += self.res_x[2] * abs(position_y)
                f32PosVarX += self.res_x[3] * (position_x * position_x)
                f32PosVarX += self.res_x[4] * (position_y * position_y)
                f32PosVarX += self.res_x[5] * abs(position_y * position_x)

                f32PosVarY = self.res_y[0]
                f32PosVarY += self.res_y[1] * abs(position_x)
                f32PosVarY += self.res_y[2] * abs(position_y)
                f32PosVarY += self.res_y[3] * (position_x * position_x)
                f32PosVarY += self.res_y[4] * (position_y * position_y)
                f32PosVarY += self.res_y[5] * abs(position_y * position_x)
                # print('fit lgt', f32PosVarX)
                # print('fit lat', f32PosVarY)


if __name__ == "__main__":
    fit = Fit()
    # fit.doFit("/Users/xieyao/Downloads/4_TYPE/gt_type_BigCar.csv", "BigCar")
    fit.doFit("/Users/xieyao/Downloads/4_TYPE/gt_type_SmallCar.csv", "SmallCar")
    fit.test()
