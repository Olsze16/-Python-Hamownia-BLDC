import matplotlib.pyplot as plt
def calculatesensors(i, x, y, y1, y2, y3, y4, data_int):
    y.append(float(data_int[0]))
    y1.append(float(data_int[1]))
    y2.append(float(data_int[2]))
    y3.append(float(data_int[3]))
    y4.append(float(data_int[4]))
    x.append(i)
    return y, y1, y2, y3, y4, x

def updateplots (ax, y, y1, y2, y3, y4, x):
    ax[0, 1].clear()
    ax[0, 0].clear()
    ax[1, 0].clear()
    ax[1, 1].clear()
    ax[0, 1].plot(x, y1)  # plot something
    ax[0, 0].plot(x, y2)  # plot something
    ax[1, 0].plot(x, y3)  # plot something
    ax[1, 1].plot(x, y4)  # plot something
    return ax
