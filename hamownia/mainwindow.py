import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import styledef
import time
import numpy as np
import json


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
staticplotv=False
set_speed = 45
set_time = 20
set_rampa = 4
set_rampcalc=2
ping =0.001
rpmset=25


#Private variables END
def testwithfft():
    global i, warthZscale, RozScaleval
    if (RozScaleval == 1): rozd = (512/2)-1
    elif (RozScaleval == 2): rozd = (1024/2)-1
    elif (RozScaleval == 3): rozd = (2048/2)-1
    elif (RozScaleval == 4): rozd = (4096/2)-1
    rozd = int(rozd)
    fft = np.zeros(rozd, dtype=float)  # x
    fft1 = np.zeros(rozd, dtype=float)  # y
    fft2 = np.zeros(rozd, dtype=float)  # z
    fft3 = np.zeros(rozd, dtype=float)  # napiecie
    fft4 = np.zeros(rozd, dtype=float)  # prad
    if(warthZscale==1): freq = np.linspace(0, 1000, num=rozd, endpoint=True)
    elif(warthZscale==2): freq = np.linspace(0, 2000, num=rozd, endpoint=True)
    elif(warthZscale==3): freq = np.linspace(0, 2500, num=rozd, endpoint=True)
    elif(warthZscale==4): freq = np.linspace(0, 4000, num=rozd, endpoint=True)
    elif(warthZscale==5): freq = np.linspace(0, 5000, num=rozd, endpoint=True)
    plt.ion()
    fig = plt.figure(figsize=(8,8))
    fig.suptitle('Analiza czasowo-częstotliwościowa FFT', fontsize=12)
    fig.canvas.set_window_title('Plotowanie FFT')
    if(xaxis == False and yaxis == False and zaxis == False and cvaxis == True):
        ax3 = fig.add_subplot(211)
        ax4 = fig.add_subplot(212)
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == False and yaxis == False and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                print(dataplot)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax3.cla()
                    ax4.cla()
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMagnitude FFT")
                    ax4.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif(xaxis == False and yaxis == False and zaxis == True and cvaxis == False):
        ax2 = fig.add_subplot(111)
        line2, = ax2.plot(freq, fft2, 'green')
        while (xaxis == False and yaxis == False and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax2.cla()
                    line2, = ax2.plot(freq, fft2, 'green')
                    ax2.set_ylim([0, 200])
                    ax2.set_ylabel("Z Axis\nMag FFT")
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
        line2, = ax2.plot(freq, fft2, 'green')
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == False and yaxis == False and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line2, = ax2.plot(freq, fft2, 'green')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft2[i] = data_intplot[2]
                fft3[i] = data_intplot[3]
                fft4[i] = data_intplot[4]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == False and cvaxis == False):
        ax1 = fig.add_subplot(111)
        line1, = ax1.plot(freq, fft1, 'red')
        while (xaxis == False and yaxis == True and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax1.cla()
                    line1, = ax1.plot(freq, fft1, 'red')
                    ax1.set_ylim([0, 200])
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft1[i] = data_intplot[1]
                i += 1
            except:
                pass
    elif (xaxis == False and yaxis == True and zaxis == False and cvaxis == True):
        ax1 = fig.add_subplot(311)
        ax3 = fig.add_subplot(312)
        ax4 = fig.add_subplot(313)
        line3, = ax3.plot(freq, fft3,'magenta')
        line4, = ax4.plot(freq, fft4,'limegreen')
        line1, = ax1.plot(freq, fft1, 'red')
        while (xaxis == False and yaxis == True and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    line1, = ax1.plot(freq, fft1, 'red')
                    ax1.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        line2, = ax2.plot(freq, fft2,'green')
        line1, = ax1.plot(freq, fft1,'red')
        while (xaxis == False and yaxis == True and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax1.cla()
                    ax2.cla()
                    line2, = ax2.plot(freq, fft2, 'green')
                    line1, = ax1.plot(freq, fft1, 'red')
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
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
        line2, = ax2.plot(freq, fft2, 'green')
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        line1, = ax1.plot(freq, fft1, 'red')
        while (xaxis == False and yaxis == True and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    ax2.cla()
                    line2, = ax2.plot(freq, fft2, 'green')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    line1, = ax1.plot(freq, fft1, 'red')
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        while (xaxis == True and yaxis == False and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    ax.set_ylim([0, 200])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    fig.canvas.draw()
                fft[i] = data_intplot[0]
                i += 1
            except:
                pass
    elif (xaxis == True and yaxis == False and zaxis == False and cvaxis == True):
        ax = fig.add_subplot(311)
        ax3 = fig.add_subplot(312)
        ax4 = fig.add_subplot(313)
        line, = ax.plot(freq, fft, 'cyan')
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == True and yaxis == False and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        line2, = ax2.plot(freq, fft2, 'green')
        while (xaxis == True and yaxis == False and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax2.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line2, = ax2.plot(freq, fft2, 'green')
                    ax.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        line2, = ax2.plot(freq, fft2, 'green')
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == True and yaxis == False and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line2, = ax2.plot(freq, fft2, 'green')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft,'cyan')
        line1, = ax1.plot(freq, fft1,'red')
        while (xaxis == True and yaxis == True and zaxis == False and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line1, = ax1.plot(freq, fft1, 'red')
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        line1, = ax1.plot(freq, fft1, 'red')
        line3, = ax3.plot(freq, fft3,'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == True and yaxis == True and zaxis == False and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line1, = ax1.plot(freq, fft1, 'red')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        line1, = ax1.plot(freq, fft1, 'red')
        line2, = ax2.plot(freq, fft2, 'green')
        while (xaxis == True and yaxis == True and zaxis == True and cvaxis == False):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax2.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line1, = ax1.plot(freq, fft1, 'red')
                    line2, = ax2.plot(freq, fft2, 'green')
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
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
        line, = ax.plot(freq, fft, 'cyan')
        line1, = ax1.plot(freq, fft1, 'red')
        line2, = ax2.plot(freq, fft2, 'green')
        line3, = ax3.plot(freq, fft3, 'magenta')
        line4, = ax4.plot(freq, fft4, 'limegreen')
        while (xaxis == True and yaxis == True and zaxis == True and cvaxis == True):
            mainwindow.update()
            try:
                dataplot = soc.recv(55)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    break
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                if i == rozd:
                    i = 0
                    ax.cla()
                    ax1.cla()
                    ax2.cla()
                    ax3.cla()
                    ax4.cla()
                    line, = ax.plot(freq, fft, 'cyan')
                    line1, = ax1.plot(freq, fft1, 'red')
                    line2, = ax2.plot(freq, fft2, 'green')
                    line3, = ax3.plot(freq, fft3, 'magenta')
                    line4, = ax4.plot(freq, fft4, 'limegreen')
                    ax.set_ylim([0, 200])
                    ax1.set_ylim([0, 200])
                    ax2.set_ylim([0, 200])
                    ax3.set_ylim([0, 2])
                    ax4.set_ylim([0, 30])
                    ax.set_ylabel("X Axis\nMag FFT")
                    ax.set_xlabel("Frequency [Hz]")
                    ax1.set_ylabel("Y Axis\nMag FFT")
                    ax1.set_xlabel("Frequency [Hz]")
                    ax2.set_ylabel("Z Axis\nMag FFT")
                    ax2.set_xlabel("Frequency [Hz]")
                    ax3.set_ylabel("Napięcie\nMag FFT")
                    ax3.set_xlabel("Frequency [Hz]")
                    ax4.set_ylabel("Prąd\nMag FFT")
                    ax4.set_xlabel("Frequency [Hz]")
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
        fig1, (ax,ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, sharex=True)
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
        line, = ax.plot(xs, ys, 'cyan')
        line1, = ax1.plot(xs, ys1, 'red')
        line2, = ax2.plot(xs, ys2, 'green')
        line3, = ax3.plot(xs, ys3, 'magenta')
        line4, = ax4.plot(xs, ys4, 'limegreen')

        plt.xlabel('Samples')

        def animate(i, ys, ys1, ys2, ys3, ys4):
            try:  # sprawdzenie czy socket dostaje dane
                dataplot = soc.recv(25)
                if (b'END' in dataplot):
                    stopbutton_clicked()
                    ys.append(float(0))
                    ys1.append(float(0))
                    ys2.append(float(0))
                    ys3.append(float(0))
                    ys4.append(float(0))
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
                else:
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
        ani = animation.FuncAnimation(fig1, animate, fargs=(ys,ys1,ys2,ys3,ys4),interval=100,blit=True, frames=6)
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
            else:
                receivedata()
    elif(sensorsread==False and dynamicplot==False and reczny==True):
        while(reczny==True):
            mainwindow.update()
            time.sleep(ping)
            rpmset = scale.get()
            rpmsetbyes = "3 " + str(rpmset)
            soc.sendto(bytes(rpmsetbyes, "utf-8"), (servIP, servPORT))
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
def static_but1():
    global staticplotv
    staticplotv = not staticplotv
    return staticplotv
def receivedata():
    global i
    mainwindow.update()
    time.sleep(ping)
    try: #sprawdzenie czy socket dostaje dane
        dataplot = soc.recv(25)
        if (b'END' in dataplot):
            stopbutton_clicked()
        else:
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
    global rpmset, reczny, soc
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
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
    welcomewindow.destroy()
    mainwindowwidget()
def startbutton_clicked():
    global set_speed, set_time, soc, set_rampcalc
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    if(set_rampcalc<10):
        stringinbytes = "1 "+ str(set_speed)+" "+str(set_time)+" 0"+str(set_rampcalc)
    else:
        stringinbytes = "1 "+ str(set_speed)+" "+str(set_time)+" "+str(set_rampcalc)
    soc.sendto(bytes(stringinbytes,  "utf-8"), (servIP, servPORT))
    showplottest_clicked()
def startfftbutton_clicked():
    global set_speed, set_time, soc, set_rampcalc, warthZscale, RozScaleval

    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    if(set_rampcalc<10):
        stringinbytes = "4 "+ str(set_speed)+" "+str(set_time)+" 0"+str(set_rampcalc)+" "+str(warthZscale)+" "+str(RozScaleval)
    else:
        stringinbytes = "4 "+ str(set_speed)+" "+str(set_time)+" "+str(set_rampcalc)+" "+str(warthZscale)+" "+str(RozScaleval)
    soc.sendto(bytes(stringinbytes,  "utf-8"), (servIP, servPORT))
    testwithfft()
def startstaticbutton_clicked():
    global set_speed, set_time, soc, set_rampcalc
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    if(set_rampcalc<10):
        stringinbytes = "5 "+ str(set_speed)+" "+str(set_time)+" 0"+str(set_rampcalc)
    else:
        stringinbytes = "5 "+ str(set_speed)+" "+str(set_time)+" "+str(set_rampcalc)
    soc.sendto(bytes(stringinbytes,  "utf-8"), (servIP, servPORT))
    statictest()
def statictest():
    global i, set_time
    numpyvalue = (int(set_time) * 10)
    empty={}
    if(staticplotv==True):
        fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True)
        ax1.set_ylabel("[A]")
        ax2.set_ylabel("[V]")
        ax3.set_ylabel("[rpm]")
        ax4.set_ylabel("[oC]")
        ax5.set_ylabel("[g]")
        ax5.set_xlabel("Samples")
        ax1.set_ylim([0,10]) #Zakres Amper na wykresie
        ax2.set_ylim([0,15]) #Zakres Voltage na wykresie
        ax3.set_ylim([0,6000]) #Zakres rpm na wykresie
        ax4.set_ylim(0,40) #zakres temp na wykresie
        ax5.set_ylim(0,200) #zakres ciag na wykresie
        current = np.zeros(numpyvalue, dtype=float)  # prad
        voltage = np.zeros(numpyvalue, dtype=float) # napiecie
        predkosc = np.zeros(numpyvalue, dtype=float) # predkosc
        temp = np.zeros(numpyvalue, dtype=float) #temp
        ciag = np.zeros(numpyvalue, dtype=float) #ciag
        samples = np.linspace(0, numpyvalue, num=numpyvalue, endpoint=True)
    with open(jsonfileloc, 'w') as f:
        json.dump(empty, f)
        f.close()
    while True:
        mainwindow.update()
        time.sleep(ping)
        try: #sprawdzenie czy socket dostaje dane
            dataplot = soc.recv(25)
            if (b'END' in dataplot):
                ax1.plot(samples,current, 'cyan')
                ax2.plot(samples,voltage, 'red')
                ax3.plot(samples,predkosc, 'green')
                ax4.plot(samples,temp, 'magenta')
                ax5.plot(samples,ciag, 'limegreen')
                stopbutton_clicked()
                plt.show()
                break
            else:
                print(dataplot)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                y = {"Numer probki": i,
                     "Prad:": data_intplot[0],
                     "Napiecie:": data_intplot[1],
                     "Predkosc:": data_intplot[2],
                     "Temperatura:": data_intplot[3],
                     "Ciag:": data_intplot[4]
                     }
                with open(jsonfileloc, 'a') as f:
                    json.dump(y, f, indent = 2)
                if(staticplotv==True):
                    current[i]=data_intplot[0]
                    voltage[i]= data_intplot[1]
                    predkosc[i]=data_intplot[2]
                    temp[i]=data_intplot[3]
                    ciag[i]=data_intplot[4]
                i += 1
        except socket.error: #jezeli socket nie dostaje danych:
            pass #zwolnienie programu w momencie, kiedy socket nie dostaje danych
def stopbutton_clicked():
    global soc, reczny,i, xaxis, zaxis, yaxis, cvaxis, dynamicplot, sensorsread,dyn,curvolt,xaxisbut1,zaxisbut1,yaxisbut1, sensbut1, staticplot, staticplotv
    soc.sendto(bytes("0",  "utf-8"), (servIP, servPORT))
    staticplotv=False
    reczny=False
    xaxis=False
    yaxis=False
    zaxis=False
    cvaxis=False
    dynamicplot=False
    sensorsread=False
    i=0
    dyn.deselect()
    xaxisbut1.deselect()
    yaxisbut1.deselect()
    zaxisbut1.deselect()
    sensbut1.deselect()
    curvolt.deselect()
    staticplot.deselect()
    soc.close()
    mainwindow.update()
def testbutton_clicked():
    global soc
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    soc.sendto(bytes("2",  "utf-8"), (servIP, servPORT))
    time.sleep(0.2)
    try:
        dataplot = soc.recv(2)
        if (dataplot==b'OK'):
            tk.messagebox.showinfo(title="Connection test", message="STM32 connected!")
            soc.close()
    except:
        tk.messagebox.showerror(title="Connection test", message="STM32 not connected")
        pass
def jsonnameget():
    global jsonfileloc, jsonNAME
    jsonfileloc=jsonNAME.get()
    tk.messagebox.showinfo(title="Potwierdzenie", message="Dane z testu zostaną zapisane do pliku o nazwie:\n" +jsonfileloc +"\nw folderze głównym projektu.")
    return jsonfileloc
def mainwindowwidget():
    #Definicja wyglądu mainwindow
    global mainwindow
    mainwindow = tk.Tk()
    tab_parent = ttk.Notebook(mainwindow, style="TNotebook")
    tab1 = ttk.Frame(tab_parent, style="Frame1.TFrame")
    tab2 = ttk.Frame(tab_parent, style="Frame1.TFrame")
    tab3 = ttk.Frame(tab_parent, style="Frame1.TFrame")
    tab_parent.add(tab1, text="Hamownia BLDC")
    tab_parent.add(tab2, text="Analiza drgań FFT")
    tab_parent.add(tab3, text="Statyczny test")
    tab_parent.grid(row=0, column=0)
    styledef.mainwindowstyle()
    mainwindow.title("Praca Inżynierska - Kamil Olszewski, Daniel Świątek")
    mainwindow.configure(bg="#bdc3c7")
    tk.Label(tab1,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2)
    tk.Label(tab2,bg="#bdc3c7", text="        Analiza FFT drgań silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2, sticky="NSEW")
    tk.Label(tab3, bg="#bdc3c7", text="Statyczny test silnika BLDC - Nucelo F7", font=("Helvetica", 16, "bold")).grid(row=0, column=2, sticky="NSEW")
    tk.Label(tab1, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(tab2, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(tab3, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(tab1,bg="#bdc3c7", text="Serwer STM32  \n Ethernet UDP \n Adres IP:"+ servIP +"\nPort:" + str(servPORT), relief="solid", font=("Arial",8)).grid(row=1, column=0, columnspan=2)
    tk.Label(tab2,bg="#bdc3c7", text="Serwer STM32  \n Ethernet UDP \n Adres IP:"+ servIP +"\nPort:" + str(servPORT), relief="solid", font=("Arial",8)).grid(row=1, column=0, columnspan=2)
    tk.Label(tab3,bg="#bdc3c7", text="Serwer STM32  \n Ethernet UDP \n Adres IP:"+ servIP +"\nPort:" + str(servPORT), relief="solid", font=("Arial",8)).grid(row=1, column=0, columnspan=2)
    tk.Label(tab1,bg="#bdc3c7", text="Python client \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)
    tk.Label(tab2,bg="#bdc3c7", text="Python client \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)
    tk.Label(tab3,bg="#bdc3c7", text="Python client \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

    #Konfiguracja przycisków do obsługi stringów wysyłanych do STM32-F7
    global dyn,xaxisbut1,zaxisbut1,yaxisbut1, sensbut1, curvolt
    ttk.Label(tab1, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    ttk.Label(tab2, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    ttk.Label(tab3, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    putlogo1=tk.PhotoImage(file='putlogo.png')
    tk.Label(tab1, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    tk.Label(tab2, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    tk.Label(tab3, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    ttk.Separator(tab1).grid(row=4, column=0, columnspan=7, ipadx=410)
    ttk.Separator(tab1).grid(row=10, column=0, columnspan=7, ipadx=410)
    ttk.Separator(tab2).grid(row=4, column=0, columnspan=7, ipadx=410)
    ttk.Separator(tab2).grid(row=10, column=0, columnspan=7, ipadx=410)
    ttk.Separator(tab3).grid(row=4, column=0, columnspan=7, ipadx=410)
    ttk.Separator(tab3).grid(row=10, column=0, columnspan=7, ipadx=410)
    ttk.Button(tab1,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    ttk.Button(tab2,text="Start BLDC", style="But1.TButton", command=startfftbutton_clicked).grid(row=5,column=2)
    ttk.Button(tab3,text="Start BLDC", style="But1.TButton", command=startstaticbutton_clicked).grid(row=5,column=2)
    dyn=tk.Checkbutton(tab1, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    dyn.grid(row=11, column=2)
    tk.Checkbutton(tab2, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab3, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    ttk.Button(tab1,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab2,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab3,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab1,text="Test połączenia", style="But6.TButton", command=testbutton_clicked).grid(row=8,column=2)
    ttk.Button(tab2,text="Test połączenia", style="But6.TButton", command=testbutton_clicked).grid(row=8,column=2)
    ttk.Button(tab3,text="Test połączenia", style="But6.TButton", command=testbutton_clicked).grid(row=8,column=2)
    ttk.Button(tab1,text="Ustawienia", style="But5.TButton", command=opensettings).grid(row=7,column=2)
    ttk.Button(tab2,text="Ustawienia", style="But5.TButton", command=opensettings).grid(row=7,column=2)
    ttk.Button(tab3,text="Ustawienia", style="But5.TButton", command=opensettings).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    global rpmset, scale, fftBUT, jsonNAME
    ttk.Label(tab1, text="Test ręczny BLDC:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab2, text="Konfiguracja plot:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab3, text="Zapis wart. do pliku:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab1, text="Prędkość zadana [% max]:", style="BW4.TLabel").grid(row=5,column=0)
    ttk.Label(tab2, text="Wybierz osie do analizy:", style="BW4.TLabel").grid(row=5,column=0)
    ttk.Label(tab3, text="Nazwa pliku .json:", style="BW4.TLabel").grid(row=5,column=0)
    jsonNAME=ttk.Entry(tab3, width=15)
    jsonNAME.grid(row=6, column=0)
    jsonNAME.insert(0,"testvalues.json")
    ttk.Button(tab3,text="Zatwierdź", style="But3.TButton", command=jsonnameget).grid(row=7, column=0)
    tk.Checkbutton(tab1, text="X AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    xaxisbut1=tk.Checkbutton(tab2, text="X AXIS", font=("Helvetica",9),command=xaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    xaxisbut1.grid(row=6,column=0,pady=4)
    tk.Checkbutton(tab3, text="X AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab3, text="Y AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab1, text="Y AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    yaxisbut1=tk.Checkbutton(tab2, text="Y AXIS", font=("Helvetica",9),command=yaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    yaxisbut1.grid(row=7, column=0, pady=3)
    tk.Checkbutton(tab1, text="Z AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab3, text="Z AXIS", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    zaxisbut1=tk.Checkbutton(tab2, text="Z AXIS", font=("Helvetica",9),command=zaxisbut, bg="#bdc3c7", activebackground="#bdc3c7")
    zaxisbut1.grid(row=8,column=0, pady=3)
    scale=tk.Scale(tab1, from_=25, to=99, resolution=1, orient=tk.HORIZONTAL,  width=12, bg='gray', bd=1,font=("Helvetica",8))
    scale.grid(row=6, column=0)
    ttk.Button(tab1,text="Start ręczny", style="But3.TButton", command=startreczny_clicked).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    ttk.Label(tab1, text="Odczyt sensorów:", style="BW.TLabel").grid(row=3, column=5, columnspan=2)
    sensbut1=tk.Checkbutton(tab1, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7")
    sensbut1.grid(row=11,column=5,columnspan=2)
    tk.Checkbutton(tab2, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab3, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7")
    ttk.Label(tab1,text="Prąd:", style="BW3.TLabel").grid(row=5, column=5, sticky="W")
    ttk.Label(tab1,text="Napięcie:", style="BW3.TLabel").grid(row=6, column=5, sticky="W")
    ttk.Label(tab1,text="Prędkość:", style="BW3.TLabel").grid(row=7, column=5, sticky="W")
    ttk.Label(tab1,text="Temperatura:", style="BW3.TLabel").grid(row=8, column=5, sticky="W")
    ttk.Label(tab1,text="Ciąg:", style="BW3.TLabel").grid(row=9, column=5, sticky="W")
    tk.Checkbutton(tab3, text="Pokaż analizę FFT\n dla prądu i napięcia", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7", command=cvaxisbut)
    curvol=tk.Checkbutton(tab1, text="Pokaż analizę FFT\n dla prądu i napięcia", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7", command=cvaxisbut)
    curvolt=tk.Checkbutton(tab2, text="Pokaż analizę FFT\n dla prądu i napięcia", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7", command=cvaxisbut)
    curvolt.grid(row=11,column=2)
    global current, voltage, rpm, temp, ciag, staticplot
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
    tk.Checkbutton(tab1, text="Pokaż statyczne wykresy\n po zakończeniu testu", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab2, text="Pokaż statyczne wykresy\n po zakończeniu testu", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
    staticplot=tk.Checkbutton(tab3, text="Pokaż statyczne wykresy\n po zakończeniu testu", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7", command=static_but1)
    staticplot.grid(row=11,column=2)
    mainwindow.resizable(0, 0)

    ## Dodatkowe v.02
    global hz, warthZscale, roz, RozScaleval
    HZScale=tk.Scale(tab2, from_=1, to=5, resolution=1, orient=tk.HORIZONTAL, width=12, bg='gray', bd=1,font=("Helvetica",8))
    HZScale.grid(row=6, column=5)
    RozScale=tk.Scale(tab2, from_=1, to=4, resolution=1, orient=tk.HORIZONTAL, width=12, bg='gray', bd=1,font=("Helvetica",8))
    RozScale.grid(row=8, column=5)
    warthZscale = HZScale.get()
    RozScaleval = RozScale.get()
    if (warthZscale==1):hz=2
    elif (warthZscale==2):hz=4
    elif (warthZscale==3):hz=5
    elif (warthZscale==4):hz=8
    elif (warthZscale==5):hz=10
    if (RozScaleval==1):roz=512
    elif (RozScaleval==2):roz=1024
    elif (RozScaleval==3):roz=2048
    elif (RozScaleval==4):roz=4096
    ttk.Label(tab2, text="Ustawienia FFT:", style="BW.TLabel").grid(row=3, column=5)
    czstring=tk.StringVar()
    czstring.set("Próbkowanie:\n" +str(hz) +" [kHz]")
    cz=ttk.Label(tab2,textvariable=czstring, style="BW4.TLabel")
    cz.grid(row=5, column=5)
    rozstring=tk.StringVar()
    rozstring.set("Rozdzielczość:\n" +str(roz) +" [samples]")
    rozl=ttk.Label(tab2,textvariable=rozstring, style="BW4.TLabel")
    rozl.grid(row=7, column=5)
    while True:
        mainwindow.update()
        warthZscale = HZScale.get()
        RozScaleval = RozScale.get()
        if (warthZscale == 1):hz = 2
        elif (warthZscale == 2):hz = 4
        elif (warthZscale == 3):hz = 5
        elif (warthZscale == 4):hz = 8
        elif (warthZscale == 5):hz = 10
        if (RozScaleval == 1):roz = 512
        elif (RozScaleval == 2):roz = 1024
        elif (RozScaleval == 3):roz = 2048
        elif (RozScaleval == 4):roz = 4096
        czstring.set("Próbkowanie:" + str(hz) + " [kHz]")
        rozstring.set("Rozdzielczość:\n" + str(roz) + " [samples]")
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
    #Promotor
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Promotor:").grid(row=8,column=0, sticky="W")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Dr inż. Dominik Łuczak").grid(row=9, column=0, sticky="W")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="ZSEP WARiE Put Poznań").grid(row=10, column=0, sticky="W")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Poznań University of Technology, 2020").grid(row=11, column=0, columnspan=2)
    welcomewindow.resizable(0,0)
    welcomewindow.mainloop()
def opensettings():
    global settings_speed, settings_time, settings, settings_rampa, set_rampa, set_time, set_speed
    settings = tk.Tk()
    styledef.welcomnewindowstyle()
    settings.title("Ustawienia")
    settings.configure(bg="#bdc3c7")
    tk.Label(settings, bg="#bdc3c7", text="Prędkość końcowa [% max]:").grid(row=0, column=0, sticky="W")
    tk.Label(settings, bg="#bdc3c7", text="Czas trwania testu [s]:").grid(row=1, column=0, sticky="W")
    tk.Label(settings, bg="#bdc3c7", text="Rampa przyśpieszenia [%/s]:").grid(row=2, column=0, sticky="W")
    settings_speed=tk.Scale(settings, from_=25, to=99, resolution=1, orient=tk.HORIZONTAL)
    settings_speed.set(set_speed)
    settings_speed.grid(row=0, column=1, sticky="E")
    settings_time=tk.Scale(settings, from_=10, to=99, resolution=1, orient=tk.HORIZONTAL)
    settings_time.grid(row=1, column=1, sticky="E")
    settings_time.set(set_time)
    settings_rampa=tk.Scale(settings, from_=2, to=20, resolution=2, orient=tk.HORIZONTAL)
    settings_rampa.grid(row=2, column=1, sticky="E")
    settings_rampa.set(set_rampa)
    tk.Button(settings, bg="#bdc3c7", text="Zatwierdź zmiany", command=acceptchanges).grid(row=3,column=0, columnspan=2)
    settings.resizable(0,0)
def acceptchanges():
    global set_speed, set_time, settings_speed, settings_time, set_rampa, settings_rampa, set_rampcalc
    set_speed = settings_speed.get()
    set_time = settings_time.get()
    set_rampa = settings_rampa.get()
    set_rampcalc = int((settings_rampa.get() - (settings_rampa.get()/2)))
    settings.destroy()
    return set_speed, set_time, set_rampa, set_rampcalc

welcomewindowwidget()

