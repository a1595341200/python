# ！/usr/bin/python3

from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
import corner
import numpy as np
ChiSquaredCdf1TableTable = [
    0.000000, 0.176937, 0.248170, 0.301465, 0.345279, 0.382925, 0.416118,
    0.445887, 0.472911, 0.497665, 0.520500, 0.541682, 0.561422, 0.579887,
    0.597216, 0.613524, 0.628907, 0.643448, 0.657218, 0.670281, 0.682689,
    0.694493, 0.705734, 0.716451, 0.726678, 0.736448, 0.745787, 0.754722,
    0.763276, 0.771472, 0.779329, 0.786865, 0.794097, 0.801041, 0.807712,
    0.814123, 0.820288, 0.826217, 0.831922, 0.837413, 0.842701, 0.847794,
    0.852701, 0.857430, 0.861989, 0.866386, 0.870626, 0.874717, 0.878665,
    0.882475, 0.886154, 0.889706, 0.893136, 0.896450, 0.899652, 0.902746,
    0.905736, 0.908626, 0.911420, 0.914122, 0.916735, 0.919263, 0.921708,
    0.924073, 0.926362, 0.928577, 0.930720, 0.932795, 0.934804, 0.936748,
    0.938631, 0.940455, 0.942220, 0.943931, 0.945588, 0.947192, 0.948747,
    0.950254, 0.951714, 0.953129, 0.954500, 0.955829, 0.957117, 0.958365,
    0.959576, 0.960750, 0.961888, 0.962991, 0.964061, 0.965099, 0.966105,
    0.967081, 0.968028, 0.968946, 0.969837, 0.970702, 0.971540, 0.972354,
    0.973143, 0.973909, 0.974653, 0.975374, 0.976074, 0.976754, 0.977413,
    0.978053, 0.978675, 0.979278, 0.979863, 0.980432, 0.980984, 0.981519,
    0.982040, 0.982545, 0.983035, 0.983511, 0.983974, 0.984423, 0.984859,
    0.985283, 0.985694, 0.986094, 0.986482, 0.986859, 0.987225, 0.987581,
    0.987926, 0.988262, 0.988588, 0.988905, 0.989213, 0.989512, 0.989802,
    0.990084, 0.990359, 0.990625, 0.990884, 0.991136, 0.991380, 0.991618,
    0.991849, 0.992073, 0.992292, 0.992504, 0.992710, 0.992910, 0.993105,
    0.993294, 0.993478, 0.993656, 0.993830, 0.993999, 0.994163, 0.994323,
    0.994478, 0.994629, 0.994775, 0.994918, 0.995057, 0.995191, 0.995322,
    0.995450, 0.995573, 0.995694, 0.995811, 0.995925, 0.996035, 0.996143,
    0.996248, 0.996350, 0.996449, 0.996545, 0.996638, 0.996729, 0.996818,
    0.996904, 0.996988, 0.997069, 0.997148, 0.997225, 0.997300, 0.997373,
    0.997444, 0.997513, 0.997580, 0.997645, 0.997708, 0.997770, 0.997830,
    0.997889, 0.997945, 0.998001, 0.998054, 0.998106, 0.998157, 0.998207,
    0.998255, 0.998302, 0.998347, 0.998392, 0.998435, 0.998477, 0.998517,
    0.998557, 0.998596, 0.998633, 0.998670, 0.998705, 0.998740, 0.998774,
    0.998806, 0.998838, 0.998869, 0.998899, 0.998929, 0.998957, 0.998985,
    0.999012, 0.999038, 0.999064, 0.999089, 0.999113, 0.999137, 0.999160,
    0.999182, 0.999204, 0.999225, 0.999246, 0.999266, 0.999285, 0.999304,
    0.999323, 0.999340, 0.999358, 0.999375, 0.999392, 0.999408, 0.999423,
    0.999439, 0.999454, 0.999468, 0.999482, 0.999496, 0.999509, 0.999522,
    0.999535, 0.999547, 0.999559, 0.999571, 0.999582, 0.999593, 0.999604,
    0.999614, 0.999624, 0.999634, 0.999644, 0.999653, 0.999663, 0.999671,
    0.999680, 0.999689, 0.999697, 0.999705, 0.999712, 0.999720, 0.999727,
    0.999735, 0.999742, 0.999748, 0.999755, 0.999761, 0.999768, 0.999774,
    0.999780, 0.999786, 0.999791, 0.999797, 0.999802, 0.999807, 0.999812,
    0.999817, 0.999822, 0.999827, 0.999831, 0.999836, 0.999840, 0.999844,
    0.999848, 0.999852, 0.999856, 0.999860, 0.999864, 0.999867, 0.999871,
    0.999874, 0.999877, 0.999880, 0.999884, 0.999887, 0.999890, 0.999892,
    0.999895, 0.999898,
]


def ChiSquaredCdf1TableFun(dist):
    step = 0.050000
    table_size = len(ChiSquaredCdf1TableTable)
    dist_ind = dist / step
    print(dist_ind)
    plt.scatter(dist_ind, 0)
    dist_int = int(dist_ind)
    w = dist_ind - dist_int
    print(w)
    plt.scatter(dist_int, ChiSquaredCdf1TableTable[dist_int])
    plt.scatter(dist_int, ChiSquaredCdf1TableTable[dist_int + 1])
    print(ChiSquaredCdf1TableTable[dist_int])
    print(ChiSquaredCdf1TableTable[dist_int + 1])
    print(ChiSquaredCdf1TableTable[dist_int] * (1 - w))
    print(ChiSquaredCdf1TableTable[dist_int + 1] * w)
    plt.show()
    if (dist_ind >= table_size - 1):
        return 1.0
    return (ChiSquaredCdf1TableTable[dist_int] * (1 - w) + ChiSquaredCdf1TableTable[dist_int + 1] * w)


def plotellipse():
    e = Ellipse(xy=(2, 1), width=5, height=3, angle=45)
    fig, ax = plt.subplots()
    ax.add_artist(e)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()


def plotcov():
    ndim, nsamples = 2, 10000
    np.random.seed(42)
    samples = np.random.randn(ndim * nsamples).reshape([nsamples, ndim])
    figure = corner.corner(samples)
    plt.show()


if __name__ == "__main__":
    # print(ChiSquaredCdf1TableFun(0.27))
    # plotellipse()
    plotcov()
