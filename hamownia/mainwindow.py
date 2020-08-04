import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import styledef
import time
import numpy as np


plt.style.use('dark_background')
#Private variables
i=0
data_int=[]
xaxis=False
yaxis=False
zaxis=False
sensorsread=False
cvaxis=False
dynamicplot=False
reczny=False
set_speed = 45
set_time = 20
ping =0.001
rpmset=25


#Private variables END
def testwithfft():
    global i
    fft = np.zeros(255, dtype=float)  # x
    fft1 = np.zeros(255, dtype=float)  # y
    fft2 = np.zeros(255, dtype=float)  # z
    fft3 = np.zeros(255, dtype=float)  # napiecie
    fft4 = np.zeros(255, dtype=float)  # prad
    freq = np.linspace(0, 2000, num=255, endpoint=True)
    plt.ion()
    fig = plt.figure(figsize=(8,8))
    if(xaxis == False and yaxis == False and zaxis == False and cvaxis == True):
        ax3 = fig.add_subplot(211)
        ax3.set_title("Koko")
        ax4 = fig.add_subplot(212)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == False and yaxis == False and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                print(dataplot)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax3.cla()
                    ax4.cla()
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax3.set_ylabel("Magnitude FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Magnitude FFT")
                    ax4.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif(xaxis == False and yaxis == False and zaxis == True and cvaxis == False):
        ax2 = fig.add_subplot(111)
        line2, = ax2.plot(freq, fft2)
        while (xaxis == False and yaxis == False and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax2.cla()
                    line2, = ax2.plot(freq, fft2)
                    ax2.set_ylim([0, 200])
                    ax2.set_ylabel("Magnitude")
                    ax2.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft2[i] = data_intplot[2]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == False and zaxis == True and cvaxis == True):
        ax2 = fig.add_subplot(311)
        ax3 = fig.add_subplot(312)
        ax4 = fig.add_subplot(313)
        line2, = ax2.plot(freq, fft2)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == False and yaxis == False and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line2, = ax2.plot(freq, fft2)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft2[i] = data_intplot[2]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == False and cvaxis == False):
        ax1 = fig.add_subplot(111)
        line1, = ax1.plot(freq, fft1)
        while (xaxis == False and yaxis == True and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax1.cla()
                    line1, = ax1.plot(freq, fft1)
                    ax1.set_ylim([0, 200])
                    fig.canvas.draw()
                fft1[i] = data_intplot[1]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == False and cvaxis == True):
        ax1 = fig.add_subplot(311)
        ax3 = fig.add_subplot(312)
        ax4 = fig.add_subplot(313)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        line1, = ax1.plot(freq, fft1)
        while (xaxis == False and yaxis == True and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    line1, = ax1.plot(freq, fft1)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax1.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft1[i] = data_intplot[1]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == True and cvaxis == False):
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        line2, = ax2.plot(freq, fft2)
        line1, = ax1.plot(freq, fft1)
        while (xaxis == False and yaxis == True and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax1.cla()
                    ax2.cla()
                    line1, = ax1.plot(freq, fft1)
                    line2, = ax2.plot(freq, fft2)
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    fig.canvas.draw()
                fft1[i] = data_intplot[1]
                fft2[i] = data_intplot[2]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == True and cvaxis == True):
        ax1 = fig.add_subplot(411)
        ax2 = fig.add_subplot(412)
        ax3 = fig.add_subplot(413)
        ax4 = fig.add_subplot(414)
        line2, = ax2.plot(freq, fft2)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        line1, = ax1.plot(freq, fft1)
        while (xaxis == False and yaxis == True and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    ax2.cla()
                    line1, = ax1.plot(freq, fft1)
                    line2, = ax2.plot(freq, fft2)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft1[i] = data_intplot[1]
                fft2[i] = data_intplot[2]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == False and zaxis == False and cvaxis == False):
        ax = fig.add_subplot(111)
        line, = ax.plot(freq, fft)
        while (xaxis == True and yaxis == False and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    line, = ax.plot(freq, fft)
                    ax.set_ylim([0, 200])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == False and zaxis == False and cvaxis == True):
        ax = fig.add_subplot(311)
        ax3 = fig.add_subplot(312)
        ax4 = fig.add_subplot(313)
        line, = ax.plot(freq, fft)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == True and yaxis == False and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == False and zaxis == True and cvaxis == False):
        ax = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        line, = ax.plot(freq, fft)
        line2, = ax2.plot(freq, fft2)
        while (xaxis == True and yaxis == False and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax2.cla()
                    line, = ax.plot(freq, fft)
                    line2, = ax2.plot(freq, fft2)
                    ax.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft2[i] = data_intplot[2]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == False and zaxis == True and cvaxis == True):
        ax = fig.add_subplot(411)
        ax2 = fig.add_subplot(412)
        ax3 = fig.add_subplot(413)
        ax4 = fig.add_subplot(414)
        line, = ax.plot(freq, fft)
        line2, = ax2.plot(freq, fft2)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == True and yaxis == False and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft)
                    line2, = ax2.plot(freq, fft2)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft2[i] = data_intplot[2]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == True and zaxis == False and cvaxis == False):
        ax = fig.add_subplot(211)
        ax1 = fig.add_subplot(212)
        line, = ax.plot(freq, fft)
        line1, = ax1.plot(freq, fft1)
        while (xaxis == True and yaxis == True and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    line, = ax.plot(freq, fft)
                    line1, = ax1.plot(freq, fft1)
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft1[i] = data_intplot[1]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == True and zaxis == False and cvaxis == True):
        ax = fig.add_subplot(411)
        ax1 = fig.add_subplot(412)
        ax3 = fig.add_subplot(413)
        ax4 = fig.add_subplot(414)
        line, = ax.plot(freq, fft)
        line1, = ax1.plot(freq, fft1)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == True and yaxis == True and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft)
                    line1, = ax1.plot(freq, fft1)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft1[i] = data_intplot[1]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == True and zaxis == True and cvaxis == False):
        ax = fig.add_subplot(311)
        ax1 = fig.add_subplot(312)
        ax2 = fig.add_subplot(313)
        line, = ax.plot(freq, fft)
        line1, = ax1.plot(freq, fft1)
        line2, = ax2.plot(freq, fft2)
        while (xaxis == True and yaxis == True and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax2.cla()
                    line, = ax.plot(freq, fft)
                    line1, = ax1.plot(freq, fft1)
                    line2, = ax2.plot(freq, fft2)
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft1[i] = data_intplot[1]
                fft2[i] = data_intplot[2]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == True and zaxis == True and cvaxis == True):
        ax = fig.add_subplot(511)
        ax1 = fig.add_subplot(512)
        ax2 = fig.add_subplot(513)
        ax3 = fig.add_subplot(514)
        ax4 = fig.add_subplot(515)
        line, = ax.plot(freq, fft)
        line1, = ax1.plot(freq, fft1)
        line2, = ax2.plot(freq, fft2)
        line3, = ax3.plot(freq, fft3)
        line4, = ax4.plot(freq, fft4)
        while (xaxis == True and yaxis == True and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == 255:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft)
                    line1, = ax1.plot(freq, fft1)
                    line2, = ax2.plot(freq, fft2)
                    line3, = ax3.plot(freq, fft3)
                    line4, = ax4.plot(freq, fft4)
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                fft1[i] = data_intplot[1]
                fft2[i] = data_intplot[2]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
def dynamicplotbox():
    global dynamicplot
    dynamicplot = not dynamicplot
    return dynamicplot
def showplottest_clicked():
    if (dynamicplot==True):
        x_len = 200  # Number of points to display
        fig, (ax,ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, sharex=True)
        ax.set_ylabel("[A]")
        ax1.set_ylabel("[V]")
        ax2.set_ylabel("[rpm]")
        ax3.set_ylabel("[oC]")
        ax4.set_ylabel("[g]")
        xs = list(range(0, 200))
        ys = [0] * x_len
        ys1 = [0] * x_len
        ys2 = [0] * x_len
        ys3 = [0] * x_len
        ys4 = [0] * x_len
        ax.set_ylim([0,10]) #Zakres Amper na wykresie
        ax1.set_ylim([0,15]) #Zakres Voltage na wykresie
        ax2.set_ylim([0,6000]) #Zakres rpm na wykresie
        ax3.set_ylim(0,40) #zakres temp na wykresie
        ax4.set_ylim(0,200) #zakres ciag na wykresie
        line, = ax.plot(xs, ys)
        line1, = ax1.plot(xs, ys1)
        line2, = ax2.plot(xs, ys2)
        line3, = ax3.plot(xs, ys3)
        line4, = ax4.plot(xs, ys4)

        plt.xlabel('Samples')

        def animate(i, ys, ys1, ys2, ys3, ys4):
            try:  # sprawdzenie czy socket dostaje dane
                dataplot = soc.recv(25)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                ys.append(float(data_intplot[0]))
                ys1.append(float(data_intplot[1]))
                ys2.append(float(data_intplot[2]))
                ys3.append(float(data_intplot[3]))
                ys4.append(float(data_intplot[4]))
                if reczny == True:
                    rpmset = scale.get()
                    rpmsetbyes = "3 " + str(rpmset)
                    soc.sendto(bytes(rpmsetbyes, "utf-8"), (servIP, servPORT))
                if(sensorsread==True):
                    current.set(str(data_intplot[0]) + str(" [A]"))
                    voltage.set(str(data_intplot[1]) + str(" [V]"))
                    rpm.set(str(data_intplot[2]) + str(" [rpm]"))
                    temp.set(str(data_intplot[3]) + str(" [C]"))
                    ciag.set(str(data_intplot[4]) + str(" [g]"))
                ys = ys[-x_len:]
                ys1 = ys1[-x_len:]
                ys2 = ys2[-x_len:]
                ys3 = ys3[-x_len:]
                ys4 = ys4[-x_len:]
                line.set_ydata(ys)
                line1.set_ydata(ys1)
                line2.set_ydata(ys2)
                line3.set_ydata(ys3)
                line4.set_ydata(ys4)
                return line, line1, line2, line3, line4,
            except socket.error:  # jezeli socket nie dostaje danych:
                ys.append(float(0))
                ys1.append(float(0))
                ys2.append(float(0))
                ys3.append(float(0))
                ys4.append(float(0))
                if(sensorsread==True):
                    current.set(str("0") + str(" [A]"))
                    voltage.set(str("0") + str(" [V]"))
                    rpm.set(str("0") + str(" [rpm]"))
                    temp.set(str("0") + str(" [C]"))
                    ciag.set(str("0") + str(" [g]"))
                ys = ys[-x_len:]
                ys1 = ys1[-x_len:]
                ys2 = ys2[-x_len:]
                ys3 = ys3[-x_len:]
                ys4 = ys4[-x_len:]
                line.set_ydata(ys)
                line1.set_ydata(ys1)
                line2.set_ydata(ys2)
                line3.set_ydata(ys3)
                line4.set_ydata(ys4)
                return line, line1, line2, line3, line4,
                pass  # zwolnienie programu w momencie, kiedy socket nie dostaje danych
        ani = animation.FuncAnimation(fig, animate, fargs=(ys,ys1,ys2,ys3,ys4),interval=100,blit=True, frames=5)
        plt.show()
    elif(sensorsread==True and dynamicplot==False):
        current.set(str("0") + str(" [A]"))
        voltage.set(str("0") + str(" [V]"))
        rpm.set(str("0") + str(" [rpm]"))
        temp.set(str("0") + str(" [C]"))
        ciag.set(str("0") + str(" [g]"))
        while(sensorsread==True):
            if reczny==True:
                rpmset = scale.get()
                rpmsetbyes = "3 " + str(rpmset)
                soc.sendto(bytes(rpmsetbyes, "utf-8"), (servIP, servPORT))
                receivedata()
            receivedata()
def changesensorsvar():
    global sensorsread
    sensorsread = not sensorsread
    return sensorsread
def xaxisbut():
    global xaxis
    xaxis = not xaxis
    return xaxis
def zaxisbut():
    global zaxis
    zaxis = not zaxis
    return zaxis
def yaxisbut():
    global yaxis
    yaxis = not yaxis
    return yaxis
def cvaxisbut():
    global cvaxis
    cvaxis = not cvaxis
    return cvaxis
def receivedata():
    mainwindow.update()
    time.sleep(ping)
    try: #sprawdzenie czy socket dostaje dane
        dataplot = soc.recv(25)
        print(dataplot)
        a_list = dataplot.split()
        map_object = map(float, a_list)
        data_intplot = list(map_object)
        current.set(str(data_intplot[0]) + str(" [A]"))
        voltage.set(str(data_intplot[1]) + str(" [V]"))
        rpm.set(str(data_intplot[2]) + str(" [rpm]"))
        temp.set(str(data_intplot[3]) + str(" [C]"))
        ciag.set(str(data_intplot[4]) +str(" [g]"))
    except socket.error: #jezeli socket nie dostaje danych:
        pass #zwolnienie programu w momencie, kiedy socket nie dostaje danych
def startreczny_clicked():
    global rpmset, reczny
    reczny=True
    rpmset = scale.get()
    rpmsetbyes = "3 " + str(rpmset)
    soc.sendto(bytes(rpmsetbyes, "utf-8"),(servIP, servPORT))
    showplottest_clicked()
def connectbutton_clicked():
    global UDP_ip, UDP_port, soc, servIP, servPORT
    UDP_ip=entryIP.get()
    UDP_port=int(entryport.get())
    servIP=servIP.get()
    servPORT=int(servPORT.get())
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    welcomewindow.destroy()
    mainwindowwidget()
def startbutton_clicked():
    global set_speed, set_time
    stringinbytes = "1 "+ str(set_speed)+" "+str(set_time)
    soc.sendto(bytes(stringinbytes,  "utf-8"), (servIP, servPORT))
    showplottest_clicked()
def startfftbutton_clicked():
    global set_speed, set_time
    stringinbytes = "4 "+ str(set_speed)+" "+str(set_time)
    soc.sendto(bytes(stringinbytes,  "utf-8"), (servIP, servPORT))
    testwithfft()
def stopbutton_clicked():
    global reczny, xaxis, zaxis, yaxis, cvaxis, dynamicplot, sensorsread,dyn,curvolt,xaxisbut1,zaxisbut1,yaxisbut1, sensbut1
    soc.sendto(bytes("0",  "utf-8"), (servIP, servPORT))
    reczny=False
    xaxis=False
    yaxis=False
    zaxis=False
    cvaxis=False
    dynamicplot=False
    sensorsread=False
    dyn.deselect()
    xaxisbut1.deselect()
    yaxisbut1.deselect()
    zaxisbut1.deselect()
    sensbut1.deselect()
    curvolt.deselect()
    mainwindow.update()
def testbutton_clicked():
    soc.sendto(bytes("2",  "utf-8"), (servIP, servPORT))
    time.sleep(0.1)
    try:
        dataplot = soc.recv(2)
        if (dataplot==b'OK'):
            tk.messagebox.showinfo(title="Connection test", message="STM32 connected!")
    except:
        tk.messagebox.showerror(title="Connection test", message="STM32 not connected")
        pass
def mainwindowwidget():
    #Definicja wyglądu mainwindow
    global mainwindow
    mainwindow = tk.Tk()
    tab_parent = ttk.Notebook(mainwindow, style="TNotebook")
    tab1 = ttk.Frame(tab_parent, style="Frame1.TFrame")
    tab2 = ttk.Frame(tab_parent, style="Frame1.TFrame")
    tab_parent.add(tab1, text="Hamownia BLDC")
    tab_parent.add(tab2, text="Analiza drgań FFT")
    tab_parent.grid(row=0, column=0)
    styledef.mainwindowstyle()
    mainwindow.title("Praca Inżynierska - Kamil Olszewski, Daniel Świątek")
    mainwindow.configure(bg="#bdc3c7")
    tk.Label(tab1,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2)
    tk.Label(tab2,bg="#bdc3c7", text="        Analiza FFT drgań silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2, sticky="NSEW")
    tk.Label(tab1, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(tab2, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(tab1,bg="#bdc3c7", text="Serwer STM32  \n Ethernet UDP \n Adres IP:"+ servIP +"\nPort:" + str(servPORT), relief="solid", font=("Arial",8)).grid(row=1, column=0, columnspan=2)
    tk.Label(tab2,bg="#bdc3c7", text="Serwer STM32  \n Ethernet UDP \n Adres IP:"+ servIP +"\nPort:" + str(servPORT), relief="solid", font=("Arial",8)).grid(row=1, column=0, columnspan=2)
    tk.Label(tab1,bg="#bdc3c7", text="Python client \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)
    tk.Label(tab2,bg="#bdc3c7", text="Python client \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

    #Konfiguracja przycisków do obsługi stringów wysyłanych do STM32-F7
    global dyn,xaxisbut1,zaxisbut1,yaxisbut1, sensbut1, curvolt
    ttk.Label(tab1, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    ttk.Label(tab2, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    putlogo1=tk.PhotoImage(file='putlogo.png')
    tk.Label(tab1, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    tk.Label(tab2, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    ttk.Separator(tab1).grid(row=4, column=0, columnspan=7, ipadx=400)
    ttk.Separator(tab1).grid(row=10, column=0, columnspan=7, ipadx=400)
    ttk.Separator(tab2).grid(row=4, column=0, columnspan=7, ipadx=400)
    ttk.Separator(tab2).grid(row=10, column=0, columnspan=7, ipadx=400)
    ttk.Button(tab1,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    ttk.Button(tab2,text="Start BLDC", style="But1.TButton", command=startfftbutton_clicked).grid(row=5,column=2)
    dyn=tk.Checkbutton(tab1, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    dyn.grid(row=11, column=2)
    tk.Checkbutton(tab2, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    ttk.Button(tab1,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab2,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab1,text="Test połączenia", style="But6.TButton", command=testbutton_clicked).grid(row=8,column=2)
    ttk.Button(tab2,text="Test połączenia", style="But6.TButton", command=testbutton_clicked).grid(row=8,column=2)
    ttk.Button(tab1,text="Ustawienia", style="But5.TButton", command=opensettings).grid(row=7,column=2)
    ttk.Button(tab2,text="Ustawienia", style="But5.TButton", command=opensettings).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    global rpmset, scale, fftBUT
    ttk.Label(tab1, text="Test ręczny BLDC:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab2, text="Konfiguracja FFT:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab1, text="Prędkość zadana [% max]:", style="BW4.TLabel").grid(row=5,column=0)
    ttk.Label(tab2, text="Wybierz osie do analizy:", style="BW4.TLabel").grid(row=5,column=0)
    tk.Checkbutton(tab1, text="X AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    xaxisbut1=tk.Checkbutton(tab2, text="X AXIS", font=("Helvetica",9),command=xaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    xaxisbut1.grid(row=6,column=0,pady=4)
    tk.Checkbutton(tab1, text="Y AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    yaxisbut1=tk.Checkbutton(tab2, text="Y AXIS", font=("Helvetica",9),command=yaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    yaxisbut1.grid(row=7, column=0, pady=3)
    tk.Checkbutton(tab1, text="Z AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    zaxisbut1=tk.Checkbutton(tab2, text="Z AXIS", font=("Helvetica",9),command=zaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    zaxisbut1.grid(row=8,column=0, pady=3)
    scale=tk.Scale(tab1, from_=25, to=99, resolution=1, orient=tk.HORIZONTAL)
    scale.grid(row=6, column=0)
    ttk.Button(tab1,text="Start ręczny", style="But3.TButton", command=startreczny_clicked).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    ttk.Label(tab1, text="Odczyt sensorów:", style="BW.TLabel").grid(row=3, column=5, columnspan=2)
    sensbut1=tk.Checkbutton(tab1, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7")
    sensbut1.grid(row=11,column=5,columnspan=2)
    tk.Checkbutton(tab2, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7")
    ttk.Label(tab1,text="Prąd:", style="BW3.TLabel").grid(row=5, column=5, sticky="W")
    ttk.Label(tab1,text="Napięcie:", style="BW3.TLabel").grid(row=6, column=5, sticky="W")
    ttk.Label(tab1,text="Prędkość:", style="BW3.TLabel").grid(row=7, column=5, sticky="W")
    ttk.Label(tab1,text="Temperatura:", style="BW3.TLabel").grid(row=8, column=5, sticky="W")
    ttk.Label(tab1,text="Ciąg:", style="BW3.TLabel").grid(row=9, column=5, sticky="W")
    curvolt=tk.Checkbutton(tab2, text="Pokaż analizę FFT\n dla prądu i napięcia", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7", command=cvaxisbut)
    curvolt.grid(row=11,column=2)
    global current, voltage, rpm, temp, ciag
    current=tk.StringVar()
    voltage=tk.StringVar()
    rpm=tk.StringVar()
    temp=tk.StringVar()
    ciag=tk.StringVar()
    ttk.Label(tab1, textvariable=current, style="BW2.TLabel").grid(row=5, column=6, sticky="E")
    ttk.Label(tab1, textvariable=voltage, style="BW2.TLabel").grid(row=6, column=6, sticky="E")
    ttk.Label(tab1, textvariable=rpm, style="BW2.TLabel").grid(row=7, column=6, sticky="E")
    ttk.Label(tab1, textvariable=temp, style="BW2.TLabel").grid(row=8, column=6, sticky="E")
    ttk.Label(tab1, textvariable=ciag, style="BW2.TLabel").grid(row=9, column=6, sticky="E")
    mainwindow.resizable(0, 0)
    while True:
        mainwindow.update()
def welcomewindowwidget():
    global entryIP, entryport, welcomewindow, servIP, servPORT
    welcomewindow = tk.Tk()
    styledef.welcomnewindowstyle()
    welcomewindow.title("Praca inżynierska - stanowisko pomiarowe BLDC")
    welcomewindow.configure(bg="#bdc3c7")
    putlogo1=tk.PhotoImage(file="put.png")
    tk.Label(master=welcomewindow, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=0, columnspan=2)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Automatyczne stanowisko pomiarowe \nwraz z analizą czasowo-częstotliwościową do badań \nwysokoobrotowych silników elektrycznych małych mocy.",justify = "center").grid(row=0, column=0, columnspan=2)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Skonfiguruj połączenie z STM32:").grid(row=2, column=0,columnspan=2)

    #Connection info + buttons
    ttk.Label(welcomewindow, style="BW.TLabel", text="Adres IP :").grid(row=3, column=0)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Port :").grid(row=4, column=0)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Adres IP (stm32) :").grid(row=5, column=0)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Port (stm32) :").grid(row=6, column=0)
    servIP=ttk.Entry(welcomewindow)
    servIP.grid(row=5, column=1)
    servIP.insert(0,"192.168.2.2")
    servPORT=ttk.Entry(welcomewindow)
    servPORT.grid(row=6, column=1)
    servPORT.insert(0,"7")
    entryIP=ttk.Entry(welcomewindow)
    entryIP.grid(row=3, column=1)
    entryIP.insert(0,"192.168.0.16")
    entryport=ttk.Entry(welcomewindow)
    entryport.grid(row=4,column=1)
    entryport.insert(0,"20001")
    ttk.Button(welcomewindow,style="But1.TButton", text="connect",command=connectbutton_clicked).grid(row=7, column=0, columnspan=2)


    #Authors
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Autorzy pracy:").grid(row=8,column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Kamil Olszewski (133657)").grid(row=9, column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Daniel Świątek (133671)").grid(row=10, column=1, sticky="E")

    welcomewindow.resizable(0,0)
    welcomewindow.mainloop()
def opensettings():
    global settings_speed, settings_time, settings
    settings = tk.Tk()
    styledef.welcomnewindowstyle()
    settings.title("Ustawienia")
    settings.configure(bg="#bdc3c7")
    tk.Label(settings, bg="#bdc3c7", text="Prędkość końcowa [% max]:").grid(row=0, column=0, sticky="W")
    tk.Label(settings, bg="#bdc3c7", text="Czas trwania testu [s]:").grid(row=1, column=0, sticky="W")
    settings_speed=tk.Scale(settings, from_=25, to=99, resolution=1, orient=tk.HORIZONTAL)
    settings_speed.set(45)
    settings_speed.grid(row=0, column=1, sticky="E")
    settings_time=tk.Scale(settings, from_=10, to=99, resolution=1, orient=tk.HORIZONTAL)
    settings_time.grid(row=1, column=1, sticky="E")
    settings_time.set(20)
    tk.Button(settings, bg="#bdc3c7", text="Zatwierdź zmiany", command=acceptchanges).grid(row=2,column=0, columnspan=2)
    settings.resizable(0,0)
def acceptchanges():
    global set_speed, set_time, settings_speed, settings_time
    set_speed = settings_speed.get()
    set_time = settings_time.get()
    settings.destroy()
    return set_speed, set_time

welcomewindowwidget()

