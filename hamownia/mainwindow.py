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
from PIL import ImageTk

plt.style.use('dark_background')
#Private variables
i=0
data_int=[]
sensorsread=False
dynamicplot=False
x=[]
y=[]
ping =0.1


#Private variables END
def dynamicplotbox():
    global dynamicplot
    dynamicplot = not dynamicplot
    return dynamicplot
def showplottest_clicked():
    if (dynamicplot==True):
        x_len = 200  # Number of points to display
        y_range = [0, 35]  # Range of possible Y values to display
        fig, (ax,ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, sharex=True)
        ax.set_ylabel("[mA]")
        ax1.set_ylabel("[V]")
        ax2.set_ylabel("[rpm]")
        ax3.set_ylabel("oC]")
        ax4.set_ylabel("[g]")
        xs = list(range(0, 200))
        ys = [0] * x_len
        ys1 = [0] * x_len
        ys2 = [0] * x_len
        ys3 = [0] * x_len
        ys4 = [0] * x_len
        ax.set_ylim(y_range)
        ax1.set_ylim(y_range)
        ax2.set_ylim(y_range)
        ax3.set_ylim(y_range)
        ax4.set_ylim(y_range)
        line, = ax.plot(xs, ys)
        line1, = ax1.plot(xs, ys1)
        line2, = ax2.plot(xs, ys2)
        line3, = ax3.plot(xs, ys3)
        line4, = ax4.plot(xs, ys4)

        plt.xlabel('Samples')

        def animate(i, ys, ys1, ys2, ys3, ys4):
            try:  # sprawdzenie czy socket dostaje dane
                dataplot = soc.recv(27)
                a_list = dataplot.split()
                map_object = map(float, a_list)
                data_intplot = list(map_object)
                ys.append(float(data_intplot[0]))
                ys1.append(float(data_intplot[1]))
                ys2.append(float(data_intplot[2]))
                ys3.append(float(data_intplot[3]))
                ys4.append(float(data_intplot[4]))
                if(sensorsread==True):
                    current.set(str(data_intplot[0]) + str(" [mA]"))
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
                    current.set(str("0") + str(" [mA]"))
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
        ani = animation.FuncAnimation(fig, animate, fargs=(ys,ys1,ys2,ys3,ys4),interval=85,blit=True)
        plt.show()
    elif(sensorsread==True and dynamicplot==False):
        current.set(str("0") + str(" [mA]"))
        voltage.set(str("0") + str(" [V]"))
        rpm.set(str("0") + str(" [rpm]"))
        temp.set(str("0") + str(" [C]"))
        ciag.set(str("0") + str(" [g]"))
        while(sensorsread==True):
            receivedata()
def changesensorsvar():
    global sensorsread
    sensorsread = not sensorsread
    return sensorsread
def receivedata():
    mainwindow.update()
    time.sleep(ping)
    try: #sprawdzenie czy socket dostaje dane
        dataplot = soc.recv(27)
        print(dataplot)
        a_list = dataplot.split()
        map_object = map(float, a_list)
        data_intplot = list(map_object)
        current.set(str(data_intplot[0]) + str(" [mA]"))
        voltage.set(str(data_intplot[1]) + str(" [V]"))
        rpm.set(str(data_intplot[2]) + str(" [rpm]"))
        temp.set(str(data_intplot[3]) + str(" [C]"))
        ciag.set(str(data_intplot[4]) +str(" [g]"))
    except socket.error: #jezeli socket nie dostaje danych:
        pass #zwolnienie programu w momencie, kiedy socket nie dostaje danych
def gauss1():
    import gauss
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
    soc.sendto(bytes("1",  "utf-8"), (servIP, servPORT))
    showplottest_clicked()
    print("Gruba jazdeczka")
    i+=1
def testbutton_clicked():
    tk.messagebox.showerror(title="Connection test", message="STM32 not connected" + str(data_int[0]))
def mainwindowwidget():
    #Definicja wyglądu mainwindow
    global mainwindow
    mainwindow = tk.Tk()
    styledef.mainwindowstyle()
    mainwindow.title("BLDC")
    mainwindow.configure(bg="#bdc3c7")
    tk.Label(mainwindow,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2)
    tk.Label(mainwindow, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(mainwindow,bg="#bdc3c7", text="Podłączono z sięcią \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

    #Konfiguracja przycisków do obsługi stringów wysyłanych do STM32-F7
    ttk.Label(mainwindow, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    putlogo1=tk.PhotoImage(file='putlogo.png')
    imagelabel=tk.Label(mainwindow, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    ttk.Separator(mainwindow).grid(row=4, column=0, columnspan=7, ipadx=400)
    ttk.Separator(mainwindow).grid(row=10, column=0, columnspan=7, ipadx=400)
    ttk.Button(mainwindow,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    tk.Checkbutton(mainwindow, text="Show dynamic plots\n during test:",font=("Helvetica",9), command=dynamicplotbox,bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11, column=2)
    ttk.Button(mainwindow,text="Stop BLDC", style="But1.TButton").grid(row=6,column=2)
    ttk.Button(mainwindow,text="Connection test", style="But1.TButton", command=testbutton_clicked).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    ttk.Label(mainwindow, text="Gaussian windows:", style="BW.TLabel").grid(row=3, column=0)
    tk.Button(mainwindow,text="Sensor 1 FFT", width=15, height=1, command = gauss1).grid(row=5, column=0)
    tk.Button(mainwindow,text="Sensor 2 FFT", width=15, height=1).grid(row=6, column=0)
    tk.Button(mainwindow,text="Sensor 3 FFT", width=15, height=1).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    ttk.Label(mainwindow, text="Odczyt sensorów:", style="BW.TLabel").grid(row=3, column=5, columnspan=2)
    tk.Checkbutton(mainwindow, text="Show dynamic sensors\n value during test", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11,column=5,columnspan=2)
    ttk.Label(mainwindow,text="Sensor 1:", style="BW3.TLabel").grid(row=5, column=5)
    ttk.Label(mainwindow,text="Sensor 2:", style="BW3.TLabel").grid(row=6, column=5)
    ttk.Label(mainwindow,text="Sensor 3:", style="BW3.TLabel").grid(row=7, column=5)
    ttk.Label(mainwindow,text="Sensor 4:", style="BW3.TLabel").grid(row=8, column=5)
    ttk.Label(mainwindow,text="Sensor 5:", style="BW3.TLabel").grid(row=9, column=5)
    tk.Checkbutton(mainwindow, text="Collect data for\n Gaussian FFT analysis", font=("Helvetica",9),command=changesensorsvar, bg="#bdc3c7", activebackground="#bdc3c7").grid(row=11,column=0)
    global current, voltage, rpm, temp, ciag
    current=tk.StringVar()
    voltage=tk.StringVar()
    rpm=tk.StringVar()
    temp=tk.StringVar()
    ciag=tk.StringVar()
    ttk.Label(mainwindow, textvariable=current, style="BW2.TLabel").grid(row=5, column=6, sticky="E")
    ttk.Label(mainwindow, textvariable=voltage, style="BW2.TLabel").grid(row=6, column=6, sticky="E")
    ttk.Label(mainwindow, textvariable=rpm, style="BW2.TLabel").grid(row=7, column=6, sticky="E")
    ttk.Label(mainwindow, textvariable=temp, style="BW2.TLabel").grid(row=8, column=6, sticky="E")
    ttk.Label(mainwindow, textvariable=ciag, style="BW2.TLabel").grid(row=9, column=6, sticky="E")
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

