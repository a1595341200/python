import numpy as np
import matplotlib.pyplot as plt
import data_fit
from mpl_toolkits.mplot3d import Axes3D

fit = data_fit.Fit()
# coefficient_x, cov_x, coefficient_y, cov_y = fit.doFit("/media/psf/Home/Downloads/data/gt_type_BigCar.csv", "BigCar")
coefficient_x, cov_x, coefficient_y, cov_y = fit.doFit("/media/psf/Home/Downloads/data/gt_type_SmallCar.csv",
                                                       "SmallCar")
myx, myy = fit.test()
mes_x, mes_y = fit.get_mes()
gtx, gty = fit.get_gt()
ex, ey = fit.get_error()
FLT_ZERO = 0
# # /** Position X */
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_0 = (-1.02657224e-01)
# # OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_1 = (0.39)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_1 = ( 1.68860255e-03)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_2 = (-2.43967658e-03)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_3 = (1.73286838e-01)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_4 = (9.80352964e-03)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_5 = (-3.78955478e+00)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_0)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MAX = (3.16230)
# /** Position X */
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_0 = (0.012)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_1 = (0.39)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_1 = (0.03)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_2 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_3 = (-0.0002)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_4 = (0.006)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MAX = (3.16230)

# /** Position Y */
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_0 = (-6.19506207e-02)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_1 = (3.04163668e-04)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_2 = (2.41319276e-03)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_3 = (-8.87880343e-02)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_4 = (1.56373742e-03)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_5 = (2.49593362e+00)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_0)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MAX = (1.0)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_0 = (0.17140)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_1 = (0.0)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_2 = (0.04)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_3 = (-0.0017)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_4 = (0.000)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MAX = (10.0)

# /** Velocity X */
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_0 = (0.83380)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_1 = (-0.0135)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_2 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_3 = (-0.0002)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_4 = (0.01120)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MAX = (4.47210)

# /** Velocity Y */
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_0 = (0.07890)

OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_0 = (0.27890)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_1 = (-0.0028)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_1 = (-0.0012)

OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_2 = (FLT_ZERO)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_3 = (0.00010)

OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_3 = (0.00013)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_4 = (0.00030)

OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_4 = (0.0015)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MIN = (OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_0)
# OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MAX = (3.23610)
OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MAX = (2.0)

FLT_ONE = 1.0
FLT_TWO = 2.0
# /** New Sensor model */
# /** Position X */
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_0 = (0.95110)
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_1 = (-0.0247)
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_2 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_3 = (0.00020)
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_4 = (0.00450)
OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_5 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_POS_X_MIN = (0.1500)
OBJLIST_RAD_SENSOR_MODEL_POS_X_MAX = (FLT_ONE)

# /* Position Y */
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_0 = (0.5242)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_1 = (-0.0028)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_2 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_3 = (0.0001)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_4 = (0.0160)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_5 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_MIN = (OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_0)
OBJLIST_RAD_SENSOR_MODEL_POS_Y_MAX = (3.16230)

# /** Velocity X */
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_0 = (1.5791)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_1 = (-0.0305)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_2 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_3 = (0.0002)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_4 = (0.0003)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_5 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_MIN = (0.057)
OBJLIST_RAD_SENSOR_MODEL_VEL_X_MAX = (FLT_TWO)

# /** Velocity Y */
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_0 = (1.87190)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_1 = (0.04293)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_2 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_3 = (0.00000)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_4 = (0.00270)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_5 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MIN = (OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_0)
OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MAX = (4.25230)

# /** Acceleration X */
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_0 = (FLT_TWO)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_1 = (-0.0356)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_2 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_3 = (0.00030)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_4 = (0.00970)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_BETA_5 = (FLT_ZERO)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_MIN = (0.75)
OBJLIST_RAD_SENSOR_MODEL_ACC_X_MAX = (FLT_TWO)

# /** Position X */
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_0 = coefficient_x[0]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_1 = coefficient_x[1]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_2 = coefficient_x[2]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_3 = coefficient_x[3]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_4 = coefficient_x[4]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_5 = coefficient_x[5]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MIN \
    = (OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MAX = (10.0)

# # /** Position X */
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_0 = (1.22500)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_1 = (0.0270)         #default (0.24120)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_2 = (FLT_ZERO)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_3 = (0.0009)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_4 = (0.0050)         #default (0.06440)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_5 = (0.009)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MIN \
#   = (OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_0)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MAX = (10.0)

# /** Position Y */
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0 = coefficient_y[0]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 = coefficient_y[1]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 = coefficient_y[2]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 = coefficient_y[3]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 = coefficient_y[4]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 = coefficient_y[5]
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MIN \
    = (OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MAX = (1.73210)
# # /** Position Y */
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0 = (0.10750)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 = (-0.0079)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 = (FLT_ZERO)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 = (0.00020)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 = (0.00500)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 = (FLT_ZERO)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MIN \
#   = (OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0)
# OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MAX = (1.73210)

# /** Velocity X */
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_0 = (3.51740)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_1 = (-0.1411)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_2 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_3 = (0.00170)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_4 = (0.01870)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MIN = (FLT_ONE)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MAX = (4.4721)

# /** Velocity Y */
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0 = (0.08500)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_1 = (0.00970)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_2 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_3 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_4 = (0.00120)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_5 = (FLT_ZERO)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MIN \
    = (OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0)
OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MAX = (2.23610)

# /** Position X */
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_0 = (0.80)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_1 = (-0.0000001)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_2 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_3 = (0.002)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_4 = (0.004)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_5 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_MIN = (OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_0)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_MAX = (5.0)

# /** Position Y */
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0 = (0.4666)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 = (-0.0000001)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 = (0.0003)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 = (0.004)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MIN = 0.5
#   = (OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MAX = (1.0)

# /** Velocity X */
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_0 = (2.51740)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_1 = (-0.1411)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_2 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_3 = (0.00100)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_4 = (0.01870)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_5 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MIN = (FLT_ONE)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MAX = (4.4721)

# /** Velocity Y */
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0 = (0.4500)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_1 = (0.0003)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_2 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_3 = (0.0003)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_4 = (0.00120)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_5 = (FLT_ZERO)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MIN = 0.4500
#   = (OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0)
OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MAX = (0.8)


# 定义1R1V方差计算函数
def compute_1R1V_variance(position_x, position_y):
    f32VelVarX = OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_0
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_1 * position_x
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_2 * position_y
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_3 * (position_x * position_x)
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_4 * (position_y * position_y)
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_5 * (position_y * position_x)
    #

    f32VelVarY = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_1 * position_x
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_2 * abs(position_y)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_3 * (position_x * position_x)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_4 * (position_y * position_y)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_5 * (position_y * position_x)

    f32PosVarX = OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_0
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_1 * position_x
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_2 * position_y
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_3 * (position_x * position_x)
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_4 * (position_y * position_y)
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_5 * (position_y * position_x)

    f32PosVarY = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 * position_x
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 * abs(position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 * (position_x * position_x)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 * (position_y * position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 * (position_y * position_x)
    # print("f32PosVarX ",f32PosVarX)
    # print("f32PosVarY ",f32PosVarY)
    return f32PosVarX, f32PosVarY, f32VelVarX, f32VelVarY


# 定义4V方差计算函数
def compute_4V_variance(position_x, position_y):
    f32VelVarX = OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_0
    f32VelVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_1 * abs(position_x)
    f32VelVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_2 * position_y
    f32VelVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_3 * (position_x * position_x)
    f32VelVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_4 * (position_y * position_y)
    f32VelVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_BETA_5 * (position_y * position_x)
    # f32VelVarX = min(OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MAX, max(OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MIN, f32VelVarX))
    #

    f32VelVarY = OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0
    f32VelVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_1 * abs(position_x)
    f32VelVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_2 * abs(position_y)
    f32VelVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_3 * (position_x * position_x)
    f32VelVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_4 * (position_y * position_y)
    f32VelVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_5 * (position_y * position_x)
    # f32VelVarY = min(OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MAX, max(OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MIN, f32VelVarY))

    f32PosVarX = OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_0
    f32PosVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_1 * position_x
    f32PosVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_2 * position_y
    f32PosVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_3 * (position_x * position_x)
    f32PosVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_4 * (position_y * position_y)
    f32PosVarX += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_BETA_5 * (position_y * position_x)
    # f32PosVarX = min(OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_MAX, max(0.1, f32PosVarX))

    f32PosVarY = OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0
    f32PosVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 * position_x
    f32PosVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 * abs(position_y)
    f32PosVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 * (position_x * position_x)
    f32PosVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 * (position_y * position_y)
    f32PosVarY += OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 * (position_y * position_x)
    # f32PosVarY = min(OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MAX, max(OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MIN, f32PosVarY))

    return f32PosVarX, f32PosVarY, f32VelVarX, f32VelVarY


# 定义camear方差计算函数
def compute_camera_car_variance(position_x, position_y):
    f32VelVarX = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_0
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_1 * (position_x)
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_2 * position_y
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_3 * (position_x * position_x)
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_4 * (position_y * position_y)
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_BETA_5 * (position_y * position_x)
    # f32VelVarX = min(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MAX, max(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MIN, f32VelVarX))
    #

    f32VelVarY = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_0
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_1 * position_x
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_2 * abs(position_y)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_3 * (position_x * position_x)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_4 * (position_y * position_y)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_BETA_5 * (position_y * position_x)
    # f32VelVarY = min(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MAX, max(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MIN, f32VelVarY))

    f32PosVarX = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_0
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_1 * abs(position_x)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_2 * abs(position_y)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_3 * (position_x * position_x)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_4 * (position_y * position_y)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_BETA_5 * abs(position_y * position_x)
    # f32PosVarX = min(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MAX, max(0.1, f32PosVarX))

    f32PosVarY = OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_0
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_1 * abs(position_x)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_2 * abs(position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_3 * (position_x * position_x)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_4 * (position_y * position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_BETA_5 * abs(position_y * position_x)
    # f32PosVarY = min(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MAX, max(OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MIN, f32PosVarY))

    return abs(f32PosVarX), abs(f32PosVarY), f32VelVarX, f32VelVarY


# 定义camear方差计算函数
def compute_camera_vru_variance(position_x, position_y):
    # OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MAX = np.full(position_x.shape,OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MAX)
    # OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MIN = np.full(position_x.shape,OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MIN)

    f32VelVarX = OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_0
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_1 * position_x
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_2 * position_y
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_3 * (position_x * position_x)
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_4 * (position_y * position_y)
    f32VelVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_BETA_5 * (position_y * position_x)
    # f32VelVarX = min(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MAX, max(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MIN, f32VelVarX))

    f32VelVarY = OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_0
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_1 * position_x
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_2 * position_y
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_3 * (position_x * position_x)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_4 * (position_y * position_y)
    f32VelVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_BETA_5 * (position_y * position_x)
    # f32VelVarY = min(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MAX, max(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MIN, f32VelVarY))

    f32PosVarX = OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_0
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_1 * position_x
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_2 * position_y
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_3 * (position_x * position_x)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_4 * (position_y * position_y)
    f32PosVarX += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_BETA_5 * (position_y * position_x)
    # f32PosVarX = min(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MAX, max(0.1, f32PosVarX))

    f32PosVarY = OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_0
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_1 * position_x
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_2 * abs(position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_3 * (position_x * position_x)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_4 * (position_y * position_y)
    f32PosVarY += OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_BETA_5 * (position_y * position_x)
    # f32PosVarY = min(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MAX, max(OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MIN, f32PosVarY))

    return f32PosVarX, f32PosVarY, f32VelVarX, f32VelVarY


# 定义radar方差计算函数
def compute_radar_variance(position_x, position_y):
    f32VelVarX = OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_0
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_1 * position_x
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_2 * position_y
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_3 * (position_x * position_x)
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_4 * (position_y * position_y)
    f32VelVarX += OBJLIST_RAD_SENSOR_MODEL_VEL_X_BETA_5 * (position_y * position_x)
    # f32VelVarX = min(OBJLIST_RAD_SENSOR_MODEL_VEL_X_MAX, max(OBJLIST_RAD_SENSOR_MODEL_VEL_X_MIN, f32VelVarX))

    f32VelVarY = OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_0
    f32VelVarY += OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_1 * position_x
    f32VelVarY += OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_2 * position_y
    f32VelVarY += OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_3 * (position_x * position_x)
    f32VelVarY += OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_4 * (position_y * position_y)
    f32VelVarY += OBJLIST_RAD_SENSOR_MODEL_VEL_Y_BETA_5 * (position_y * position_x)
    # f32VelVarY = min(OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MAX, max(OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MIN, f32VelVarY))

    f32PosVarX = OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_0
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_1 * position_x
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_2 * position_y
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_3 * (position_x * position_x)
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_4 * (position_y * position_y)
    f32PosVarX += OBJLIST_RAD_SENSOR_MODEL_POS_X_BETA_5 * (position_y * position_x)
    # f32PosVarX = min(OBJLIST_RAD_SENSOR_MODEL_POS_X_MAX, max(OBJLIST_RAD_SENSOR_MODEL_POS_X_MIN, f32PosVarX))

    f32PosVarY = OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_0
    f32PosVarY += OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_1 * position_x
    f32PosVarY += OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_2 * abs(position_y)
    f32PosVarY += OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_3 * (position_x * position_x)
    f32PosVarY += OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_4 * (position_y * position_y)
    f32PosVarY += OBJLIST_RAD_SENSOR_MODEL_POS_Y_BETA_5 * (position_y * position_x)
    # f32PosVarY = min(OBJLIST_RAD_SENSOR_MODEL_POS_Y_MAX, max(OBJLIST_RAD_SENSOR_MODEL_POS_Y_MIN, f32PosVarY))

    return f32PosVarX, f32PosVarY, f32VelVarX, f32VelVarY


# 计算方差
pos_var_x_values = []
pos_var_y_values = []
vel_var_x_values = []
vel_var_y_values = []
# 生成一系列位置值
positionsX = np.linspace(0, 100, 800)
positionsY = np.linspace(-20, 20, 400)

X = []
Y = []

X, Y = np.meshgrid(positionsX, positionsY)
# CAMERA VRU
pos_var_x_values, pos_var_y_values, vel_var_x_values, vel_var_y_values = compute_camera_vru_variance(X,
                                                                                                     Y)  # 这里仅以相同的位置作为示例
vel_var_x_values = np.clip(vel_var_x_values, OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_X_MAX)
vel_var_y_values = np.clip(vel_var_y_values, OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_VEL_Y_MAX)
pos_var_x_values = np.clip(pos_var_x_values, OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_X_MAX)
pos_var_y_values = np.clip(pos_var_y_values, OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_PEDESTRIAN_POS_Y_MAX)

EVX = np.array(vel_var_x_values)
EVY = np.array(vel_var_y_values)
EX = np.array(pos_var_x_values)
EY = np.array(pos_var_y_values)

# # 绘制3D散点图
fig0 = plt.figure()
ax1 = fig0.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, EX, cmap=plt.cm.winter)
ax1.set_xlabel('Position X')
ax1.set_ylabel('Position Y')
ax1.set_zlabel('Variance')
ax1.set_title('ERROR_X')

ax2 = fig0.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, EY, cmap=plt.cm.winter)
ax2.set_xlabel('Position X')
ax2.set_ylabel('Position Y')
ax2.set_zlabel('Variance')
ax2.set_title('ERROR_Y')

ax3 = fig0.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, EVX, cmap=plt.cm.winter)
ax3.set_xlabel('Position X')
ax3.set_ylabel('Position Y')
ax3.set_zlabel('Variance')
ax3.set_title('ERROR_VX')

ax4 = fig0.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, EVY, cmap=plt.cm.winter)
ax4.set_xlabel('Position X')
ax4.set_ylabel('Position Y')
ax4.set_zlabel('Variance')
ax4.set_title('ERROR_VY')

plt.tight_layout()
fig0.canvas.set_window_title('camera vru')
# plt.show()


# CAMERA CAR
pos_var_x_values, pos_var_y_values, vel_var_x_values, vel_var_y_values = compute_camera_car_variance(X,
                                                                                                     Y)  # 这里仅以相同的位置作为示例
vel_var_x_values = np.clip(vel_var_x_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_X_MAX)
vel_var_y_values = np.clip(vel_var_y_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MAX)
# pos_var_x_values = np.clip(pos_var_x_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MIN,
#                            OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_X_MAX)
# pos_var_y_values = np.clip(pos_var_y_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MIN,
#                            OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MAX)

EVX = np.array(vel_var_x_values)
EVY = np.array(vel_var_y_values)
EX = np.array(pos_var_x_values)
EY = np.array(pos_var_y_values)


# # 绘制3D散点图
fig1 = plt.figure()
ax1 = fig1.add_subplot(121, projection='3d')
# ax1 = fig1.add_subplot(121)
ax1.plot_surface(X, Y, EX, cmap=plt.cm.winter)
# ax1.scatter(ex, ey)
# ax1.scatter(mes_x - myx, mes_y - myy)
ax1.set_xlabel('Position X')
ax1.set_ylabel('Position Y')
ax1.set_zlabel('Variance')
ax1.set_title('ERROR_X')
#
ax2 = fig1.add_subplot(122, projection='3d')
# ax2 = fig1.add_subplot(122)
# ax2.scatter(np.array(ex) - np.array(myx), np.array(ey) - np.array(myy))
ax2.plot_surface(X, Y, EY, cmap=plt.cm.winter)
ax2.set_xlabel('Position X')
ax2.set_ylabel('Position Y')
ax2.set_zlabel('Variance')
ax2.set_title('ERROR_Y')

# ax3 = fig1.add_subplot(223, projection='3d')
# ax3.plot_surface(X, Y, EVX, cmap=plt.cm.winter)
# ax3.set_xlabel('Position X')
# ax3.set_ylabel('Position Y')
# ax3.set_zlabel('Variance')
# ax3.set_title('ERROR_VX')
#
# ax4 = fig1.add_subplot(224, projection='3d')
# ax4.plot_surface(X, Y, EVY, cmap=plt.cm.winter)
# ax4.set_xlabel('Position X')
# ax4.set_ylabel('Position Y')
# ax4.set_zlabel('Variance')
# ax4.set_title('ERROR_VY')

fig1.canvas.set_window_title('camera car')

plt.tight_layout()

# plt.show()


# RADAR
pos_var_x_values, pos_var_y_values, vel_var_x_values, vel_var_y_values = compute_radar_variance(X, Y)  # 这里仅以相同的位置作为示例
vel_var_x_values = np.clip(vel_var_x_values, OBJLIST_RAD_SENSOR_MODEL_VEL_X_MIN, OBJLIST_RAD_SENSOR_MODEL_VEL_X_MAX)
vel_var_y_values = np.clip(vel_var_y_values, OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MIN, OBJLIST_RAD_SENSOR_MODEL_VEL_Y_MAX)
pos_var_x_values = np.clip(pos_var_x_values, OBJLIST_RAD_SENSOR_MODEL_POS_X_MIN, OBJLIST_RAD_SENSOR_MODEL_POS_X_MAX)
pos_var_y_values = np.clip(pos_var_y_values, OBJLIST_RAD_SENSOR_MODEL_POS_Y_MIN, OBJLIST_RAD_SENSOR_MODEL_POS_Y_MAX)

EVX = np.array(vel_var_x_values)
EVY = np.array(vel_var_y_values)
EX = np.array(pos_var_x_values)
EY = np.array(pos_var_y_values)

# # 绘制3D散点图
fig2 = plt.figure()
ax1 = fig2.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, EX, cmap=plt.cm.winter)
ax1.set_xlabel('Position X')
ax1.set_ylabel('Position Y')
ax1.set_zlabel('Variance')
ax1.set_title('ERROR_X')

ax2 = fig2.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, EY, cmap=plt.cm.winter)
ax2.set_xlabel('Position X')
ax2.set_ylabel('Position Y')
ax2.set_zlabel('Variance')
ax2.set_title('ERROR_Y')

ax3 = fig2.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, EVX, cmap=plt.cm.winter)
ax3.set_xlabel('Position X')
ax3.set_ylabel('Position Y')
ax3.set_zlabel('Variance')
ax3.set_title('ERROR_VX')

ax4 = fig2.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, EVY, cmap=plt.cm.winter)
ax4.set_xlabel('Position X')
ax4.set_ylabel('Position Y')
ax4.set_zlabel('Variance')
ax4.set_title('ERROR_VY')

plt.tight_layout()
fig2.canvas.set_window_title('radar')

# 4V
pos_var_x_values, pos_var_y_values, vel_var_x_values, vel_var_y_values = compute_4V_variance(X, Y)  # 这里仅以相同的位置作为示例
vel_var_x_values = np.clip(vel_var_x_values, OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MIN,
                           OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_X_MAX)
vel_var_y_values = np.clip(vel_var_y_values, OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MIN,
                           OBJLIST_4V_SENSOR_MODEL_VEHICLE_VEL_Y_MAX)
pos_var_x_values = np.clip(pos_var_x_values, OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_MIN,
                           OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_X_MAX)
pos_var_y_values = np.clip(pos_var_y_values, OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MIN,
                           OBJLIST_4V_SENSOR_MODEL_VEHICLE_POS_Y_MAX)

EVX = np.array(vel_var_x_values)
EVY = np.array(vel_var_y_values)
EX = np.array(pos_var_x_values)
EY = np.array(pos_var_y_values)

# # 绘制3D散点图
fig3 = plt.figure()
ax1 = fig3.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, EX, cmap=plt.cm.winter)
ax1.set_xlabel('Position X')
ax1.set_ylabel('Position Y')
ax1.set_zlabel('Variance')
ax1.set_title('ERROR_X')

ax2 = fig3.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, EY, cmap=plt.cm.winter)
ax2.set_xlabel('Position X')
ax2.set_ylabel('Position Y')
ax2.set_zlabel('Variance')
ax2.set_title('ERROR_Y')

ax3 = fig3.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, EVX, cmap=plt.cm.winter)
ax3.set_xlabel('Position X')
ax3.set_ylabel('Position Y')
ax3.set_zlabel('Variance')
ax3.set_title('ERROR_VX')

ax4 = fig3.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, EVY, cmap=plt.cm.winter)
ax4.set_xlabel('Position X')
ax4.set_ylabel('Position Y')
ax4.set_zlabel('Variance')
ax4.set_title('ERROR_VY')

plt.tight_layout()
fig3.canvas.set_window_title('4V')

# 1R1V
pos_var_x_values, pos_var_y_values, vel_var_x_values, vel_var_y_values = compute_1R1V_variance(X, Y)  # 这里仅以相同的位置作为示例
vel_var_x_values = np.clip(vel_var_x_values, OBJLIST_RAD_SENSOR_MODEL_VEL_X_MIN, OBJLIST_RAD_SENSOR_MODEL_VEL_X_MAX)
vel_var_y_values = np.clip(vel_var_y_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_VEHICLE_VEL_Y_MAX)
pos_var_x_values = np.clip(pos_var_x_values, OBJLIST_RAD_SENSOR_MODEL_POS_X_MIN, OBJLIST_RAD_SENSOR_MODEL_POS_X_MAX)
pos_var_y_values = np.clip(pos_var_y_values, OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MIN,
                           OBJLIST_MVS_SENSOR_MODEL_VEHICLE_POS_Y_MAX)

EVX = np.array(vel_var_x_values)
EVY = np.array(vel_var_y_values)
EX = np.array(pos_var_x_values)
EY = np.array(pos_var_y_values)

# # 绘制3D散点图
fig4 = plt.figure()
ax1 = fig4.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, EX, cmap=plt.cm.winter)
ax1.set_xlabel('Position X')
ax1.set_ylabel('Position Y')
ax1.set_zlabel('Variance')
ax1.set_title('ERROR_X')

ax2 = fig4.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, EY, cmap=plt.cm.winter)
ax2.set_xlabel('Position X')
ax2.set_ylabel('Position Y')
ax2.set_zlabel('Variance')
ax2.set_title('ERROR_Y')

ax3 = fig4.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, EVX, cmap=plt.cm.winter)
ax3.set_xlabel('Position X')
ax3.set_ylabel('Position Y')
ax3.set_zlabel('Variance')
ax3.set_title('ERROR_VX')

ax4 = fig4.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, EVY, cmap=plt.cm.winter)
ax4.set_xlabel('Position X')
ax4.set_ylabel('Position Y')
ax4.set_zlabel('Variance')
ax4.set_title('ERROR_VY')

plt.tight_layout()
fig4.canvas.set_window_title('1R1V')

plt.show()
