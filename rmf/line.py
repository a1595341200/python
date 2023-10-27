# /usr/bin/python3.8

import matplotlib.pyplot as plt
import pandas as pd


# 按行读取读取csv

def read_csv():
    # 读取
    csv_result = pd.read_csv('/home/user/python/rmf/RMF_Refline.csv')
    row_list = csv_result.values.tolist()
    return row_list


row_list = read_csv()


def getframe(i):
    x = []
    y = []
    print("getframe", i)
    index = 1
    print(row_list[i])
    for i in row_list[i]:
        if index % 2 == 0:
            y.append(i)
        else:
            x.append(i)
        index += 1
    return x, y


fig = plt.figure()
plt.ion()

if __name__ == "__main__":
    i = 0
    while i < len(row_list):
        print("start", i)
        fig.clf()
        # timer = fig.canvas.new_timer(interval = 10)
        # timer.add_callback(plt.close)
        x, y = getframe(i)
        i = i + 1
        if y[0] < 0.01:
            print(y[0])
            continue
        else:
            plt.legend(loc='best')
            ax = plt.gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.spines['bottom'].set_position(('data', 0))
            ax.spines['left'].set_position(('data', 0))
            ax.spines['left'].set_position(('axes', 0))
            plt.scatter(x, y)
            print(x)
            print("-------")
            print(y)
            plt.pause(0.005)
    plt.ioff()
    plt.show()
