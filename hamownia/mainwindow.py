import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
import matplotlib
from matplotlib import pyplot as plt
from plotsensors import calculatesensors
import styledef

plt.style.use('dark_background')
#Private variables
i=0
data_int=[]
x=[]
y=[]
y1=[]
y2=[]
y3=[]
y4=[]

#Private variables END
def showplot_clicked():
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True)
    fig.suptitle('Aligning x-axis using sharex')
    ax1.plot(x, y)
    ax2.plot(x ,y1)
    ax3.plot(x ,y2)
    ax4.plot(x ,y3)
    ax5.plot(x ,y4)
    fig.show()
def connectbutton_clicked():
    global UDP_ip, UDP_port, soc
    UDP_ip=entryIP.get()
    UDP_port=int(entryport.get())
    soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((UDP_ip,UDP_port))
    soc.setblocking(0)
    welcomewindow.destroy()
    mainwindowwidget()
def startbutton_clicked():
    global i
    i+=1
def testbutton_clicked():
    tk.messagebox.showerror(title="Connection test", message="STM32 not connected" + str(data_int[0]))
def mainwindowwidget():
    #Definicja wyglądu mainwindow
    mainwindow = tk.Tk()
    styledef.mainwindowstyle()
    mainwindow.configure(bg="#bdc3c7")
    mainwindow.title("BLDC")
    putlogo=tk.PhotoImage(file="put.png")
    tk.Label(mainwindow, image=putlogo, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    tk.Label(mainwindow,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2)
    tk.Label(mainwindow, text="", bg="#bdc3c7").grid(row=2, column=2)
    tk.Label(mainwindow,bg="#bdc3c7", text="Podłączono z sięcią \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

    #Konfiguracja przycisków do obsługi stringów wysyłanych do STM32-F7
    ttk.Label(mainwindow, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    ttk.Button(mainwindow,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    ttk.Button(mainwindow,text="Stop BLDC", style="But1.TButton").grid(row=6,column=2)
    ttk.Button(mainwindow,text="Connection test", style="But1.TButton", command=testbutton_clicked).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    ttk.Label(mainwindow, text="Gaussian windows:", style="BW.TLabel").grid(row=3, column=0)
    tk.Button(mainwindow,text="Sensor 1 FFT", width=15, height=1).grid(row=5, column=0)
    tk.Button(mainwindow,text="Sensor 2 FFT", width=15, height=1).grid(row=6, column=0)
    tk.Button(mainwindow,text="Sensor 3 FFT", width=15, height=1).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    ttk.Label(mainwindow, text="Odczyt z sensorów:", style="BW.TLabel").grid(row=3, column=5,columnspan=2)
    ttk.Label(mainwindow,text="Sensor 1:", style="BW3.TLabel").grid(row=5, column=5)
    ttk.Label(mainwindow,text="Sensor 2:", style="BW3.TLabel").grid(row=6, column=5)
    ttk.Label(mainwindow,text="Sensor 3:", style="BW3.TLabel").grid(row=7, column=5)
    ttk.Label(mainwindow,text="Sensor 4:", style="BW3.TLabel").grid(row=8, column=5)
    ttk.Label(mainwindow,text="Sensor 5:", style="BW3.TLabel").grid(row=9, column=5)
    ttk.Button(mainwindow, text="Show plots", style="But2.TButton", command=showplot_clicked).grid(row=10,column=5,columnspan=2, sticky="E")
    mainwindow.resizable(0, 0)
    while True:
        global data_int, i
        mainwindow.update()
        try: #sprawdzenie czy socket dostaje dane
            data = soc.recv(1024 * 10)
            a_list = data.split()
            map_object = map(int, a_list)
            data_int = list(map_object)
            ttk.Label(mainwindow, text=str(data_int[0]) + " [rpm]", style="BW2.TLabel").grid(row=5, column=6,sticky="E")
            ttk.Label(mainwindow, text=str(data_int[1]) + " [mA]", style="BW2.TLabel").grid(row=6, column=6, sticky="E")
            ttk.Label(mainwindow, text=str(data_int[2]) + " [V]", style="BW2.TLabel").grid(row=7, column=6, sticky="E")
            ttk.Label(mainwindow, text=str(data_int[3]) + " [V]", style="BW2.TLabel").grid(row=8, column=6, sticky="E")
            ttk.Label(mainwindow, text=str(data_int[4])+ " [V]", style="BW2.TLabel").grid(row=9, column=6, sticky="E")
            calculatesensors(i, x, y, y1, y2, y3, y4, data_int)
            i += 0.1
        except socket.error: #jezeli socket nie dostaje danych:
            pass #zwolnienie programu w momencie, kiedy socket nie dostaje danych
def welcomewindowwidget():
    global entryIP, entryport, welcomewindow
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
    entryIP=ttk.Entry(welcomewindow)
    entryIP.grid(row=3, column=1)
    entryIP.insert(0,"192.168.0.16")
    entryport=ttk.Entry(welcomewindow)
    entryport.grid(row=4,column=1)
    entryport.insert(0,"20001")
    ttk.Button(welcomewindow,style="But1.TButton", text="connect",command=connectbutton_clicked).grid(row=5, column=0, columnspan=2)


    #Authors
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Autorzy pracy:").grid(row=6,column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Kamil Olszewski (133657)").grid(row=7, column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Daniel Świątek (133671)").grid(row=8, column=1, sticky="E")

    welcomewindow.resizable(0,0)
    welcomewindow.mainloop()

welcomewindowwidget()

