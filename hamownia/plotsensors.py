
def calculatesensors(i, x, y, y1, y2, y3, y4, data_int):
    y.append(float(data_int[0]))
    y1.append(float(data_int[1]))
    y2.append(float(data_int[2]))
    y3.append(float(data_int[3]))
    y4.append(float(data_int[4]))
    x.append(i)
    return y, y1, y2, y3, y4, x