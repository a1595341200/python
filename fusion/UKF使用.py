import matplotlib.pyplot as plt
import numpy as np
import filterpy.common
from filterpy.kalman import MerweScaledSigmaPoints
from filterpy.kalman import UnscentedKalmanFilter
from numpy.random import randn


def fx(x, dt):
    F = np.array([[1, dt, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, dt],
                  [0, 0, 0, 1]], dtype=float)
    return np.dot(F, x)


def hx(x):
    # measurement function - convert state into a measurement
    # where measurements are [x_pos, y_pos]
    return np.array([x[0], x[2]])


dt = 0.1
points = MerweScaledSigmaPoints(4, alpha=0.1, beta=0.2, kappa=0.2)
kf = UnscentedKalmanFilter(dim_x=4, dim_z=2, dt=dt, fx=fx, hx=hx, points=points)
kf.x = np.array([-1., 1., -1, -1])  # initial state
kf.P *= 0.2  # initial uncertainty
z_std = 0.1
kf.R = np.diag([z_std ** 2, z_std ** 2])  # 1 standard
kf.Q = filterpy.common.Q_discrete_white_noise(dim=2, dt=dt, var=0.01 ** 2, block_size=2)

zs = [[i + randn() * z_std, i + randn() * z_std] for i in range(500)]  # measurements
realz = [[i, i] for i in range(500)]

resx = []
resy = []
reszx = []
reszy = []

# print(zs)
for z in zs:
    kf.predict()
    kf.update(z)
    resx.append(kf.x_post[0])
    resy.append(kf.x_post[2])
    reszx.append(z[0])
    reszy.append(z[1])
plt.subplot(1, 3, 1)
plt.plot(resx, resy)
plt.plot(reszx, reszy)
ex = [[resx[i] - realz[i][0]] for i in range(len(resx))]
ey = [[resy[i] - realz[i][1]] for i in range(len(resy))]
plt.subplot(1, 3, 2)
plt.plot(reszx, ex)
plt.subplot(1, 3, 3)
plt.plot(reszy, ey)
plt.show()
