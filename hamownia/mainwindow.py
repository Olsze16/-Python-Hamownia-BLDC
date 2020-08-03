import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
import matplotlib
from matplotlib import pyplot as plt
from plotsensors import calculatesensors, updateplots
import matplotlib.animation as animation
import styledef
import time
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

plt.style.use('dark_background')
#Private variables
i=0
data_int=[]
xaxis=False
yaxis=False
zaxis=False
sensorsread=False
fftread=False
dynamicplot=False
reczny=False
x=[]
y=[]
ping =0.001
rpmset=25


#Private variables END
def testwithfft():
    global i
    fft = np.zeros(255, dtype=float)
    fft1 = np.zeros(255, dtype=float)
    fft2 = np.zeros(255, dtype=float)
    freq = np.arange(start=0, stop=255, step=1)
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(311)
    ax1 = fig.add_subplot(312)
    ax2 = fig.add_subplot(313)
    line1, = ax.plot(freq, fft)
    line2, = ax1.plot(freq, fft1)
    line3, = ax2.plot(freq, fft2)
    while(fftread==True):
        mainwindow.update()
        try:
            dataplot = soc.recv(36)
            a_list = dataplot.split()
            map_object = map(float, a_list)
            data_intplot = list(map_object)
            print(dataplot)
            if i==255:
                print(dataplot)
                i=0
                ax1.cla()
                ax.cla()
                ax2.cla()
                line1, = ax.plot(freq, fft)
                line2, = ax1.plot(freq, fft1)
                line3, = ax2.plot(freq, fft2)
                ax.set_ylim([0, 2])
                ax1.set_ylim([0, 2])
                ax2.set_ylim([0, 2])
                fig.canvas.draw()
            fft[i]=data_intplot[0]
            fft1[i]=data_intplot[1]
            fft2[i]=data_intplot[2]
            i+=1
        except:
            pass #elobenc
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
def fftbuttonvar():
    global fftread
    fftread = not fftread
    return fftread
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
    global i
    if(fftread==True):
        soc.sendto(bytes("4",  "utf-8"), (servIP, servPORT))
        testwithfft()
        i+=1
    else:
        soc.sendto(bytes("1",  "utf-8"), (servIP, servPORT))
        showplottest_clicked()
        i+=1
def stopbutton_clicked():
    global reczny, fftBUT, fftread
    soc.sendto(bytes("0",  "utf-8"), (servIP, servPORT))
    reczny=False
    #fftBUT.deselect()
    #fftread=False
    mainwindow.update()
def testbutton_clicked():
    tk.messagebox.showerror(title="Connection test", message="STM32 not connected" + str(data_int[0]))
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
    ttk.Button(tab2,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    tk.Checkbutton(tab1, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11, column=2)
    tk.Checkbutton(tab2, text="Dynamiczne charakterystyki\n podczas testu",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7")
    ttk.Button(tab1,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab2,text="Stop BLDC", style="But4.TButton", command=stopbutton_clicked).grid(row=6,column=2)
    ttk.Button(tab1,text="Test połączenia", style="But1.TButton", command=testbutton_clicked).grid(row=7,column=2)
    ttk.Button(tab2,text="Test połączenia", style="But1.TButton", command=testbutton_clicked).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    global rpmset, scale, fftBUT
    ttk.Label(tab1, text="Test ręczny BLDC:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab2, text="Konfiguracja FFT:", style="BW.TLabel").grid(row=3, column=0)
    ttk.Label(tab1, text="Prędkość zadana [% max]:", style="BW4.TLabel").grid(row=5,column=0)
    ttk.Label(tab2, text="Wybierz osie do analizy:", style="BW4.TLabel").grid(row=5,column=0)
    tk.Checkbutton(tab1, text="X AXIS", font=("Helvetica",9),command=xaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab2, text="X AXIS", font=("Helvetica",9),command=xaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7").grid(row=6,column=0,pady=4)
    tk.Checkbutton(tab1, text="Y AXIS", font=("Helvetica",9),command=yaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab2, text="Y AXIS", font=("Helvetica",9),command=yaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7").grid(row=7, column=0, pady=3)
    tk.Checkbutton(tab1, text="Z AXIS", font=("Helvetica",9),command=zaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7")
    tk.Checkbutton(tab2, text="Z AXIS", font=("Helvetica",9),command=zaxisbut(), bg="#bdc3c7", activebackground="#bdc3c7").grid(row=8,column=0, pady=3)
    scale=tk.Scale(tab1, from_=25, to=99, resolution=1, orient=tk.HORIZONTAL)
    scale.grid(row=6, column=0)
    ttk.Button(tab1,text="Start ręczny", style="But3.TButton", command=startreczny_clicked).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    ttk.Label(tab1, text="Odczyt sensorów:", style="BW.TLabel").grid(row=3, column=5, columnspan=2)
    ttk.Label(tab2, text="Odczyt sensorów:", style="BW.TLabel").grid(row=3, column=5, columnspan=2)
    tk.Checkbutton(tab1, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11,column=5,columnspan=2)
    tk.Checkbutton(tab2, text="Odczytuj wartość sensorów\n podczas testu", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11,column=5,columnspan=2)
    ttk.Label(tab1,text="Prąd:", style="BW3.TLabel").grid(row=5, column=5, sticky="W")
    ttk.Label(tab1,text="Napięcie:", style="BW3.TLabel").grid(row=6, column=5, sticky="W")
    ttk.Label(tab1,text="Prędkość:", style="BW3.TLabel").grid(row=7, column=5, sticky="W")
    ttk.Label(tab1,text="Temperatura:", style="BW3.TLabel").grid(row=8, column=5, sticky="W")
    ttk.Label(tab1,text="Ciąg:", style="BW3.TLabel").grid(row=9, column=5, sticky="W")
    ttk.Label(tab2,text="Prąd:", style="BW3.TLabel").grid(row=5, column=5, sticky="W")
    ttk.Label(tab2,text="Napięcie:", style="BW3.TLabel").grid(row=6, column=5, sticky="W")
    ttk.Label(tab2,text="Prędkość:", style="BW3.TLabel").grid(row=7, column=5, sticky="W")
    ttk.Label(tab2,text="Temperatura:", style="BW3.TLabel").grid(row=8, column=5, sticky="W")
    ttk.Label(tab2,text="Ciąg:", style="BW3.TLabel").grid(row=9, column=5, sticky="W")
    curvolt=tk.Checkbutton(tab2, text="Pokaż analizę FFT\n dla prądu i napięcia", font=("Helvetica",9), bg="#bdc3c7", activebackground="#bdc3c7")
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
    ttk.Label(tab2, textvariable=current, style="BW2.TLabel").grid(row=5, column=6, sticky="E")
    ttk.Label(tab2, textvariable=voltage, style="BW2.TLabel").grid(row=6, column=6, sticky="E")
    ttk.Label(tab2, textvariable=rpm, style="BW2.TLabel").grid(row=7, column=6, sticky="E")
    ttk.Label(tab2, textvariable=temp, style="BW2.TLabel").grid(row=8, column=6, sticky="E")
    ttk.Label(tab2, textvariable=ciag, style="BW2.TLabel").grid(row=9, column=6, sticky="E")
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

welcomewindowwidget()

