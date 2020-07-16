import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
import numpy as np
import matplotlib
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Private variables
i=0
data_int = []
y = np.zeros(100)
y1 = np.zeros(100)
y2 = np.zeros(100)
x = np.arange(0.0,10.0,0.1)
fig = Figure(figsize=(7, 2), dpi=100)
signal =0

#Private variables END

def rysuj_plot():
    global i, x, y, fig, signal
    y[i]=float(data_int[1])
    y1[i]=float(data_int[2])
    y2[i]=float(data_int[3])
    i+=1
    signal=0
    if i==100:
        i=0
        signal=1
        fig.add_subplot(131).plot(x, y)
        fig.add_subplot(132).plot(x, y1)
        fig.add_subplot(133).plot(x, y2)
        return fig, signal

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
    mainwindow.configure(bg="#bdc3c7")
    mainwindow.title("BLDC")
    putlogo=tk.PhotoImage(file="put.png")
    tk.Label(mainwindow, image=putlogo, background="#bdc3c7", relief="solid").grid(row=1, column=2)
    tk.Label(mainwindow,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16, "bold")).grid(row=0,column=2)
    tk.Label(mainwindow, text="", bg="#bdc3c7").grid(row=2, column=2)
    lbl2 =tk.Label(mainwindow,bg="#bdc3c7", text="Podłączono z sięcią \n Ethernet UDP \n Adres IP:"+ UDP_ip +"\nPort:" + str(UDP_port), relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

    #Definicja stylu
    # text
    labelstyle = ttk.Style()
    labelstyle.configure("BW.TLabel", foreground="black",background="#bdc3c7", font=("Helvetica",10))
     #sub-def values real
    labelstyle1 = ttk.Style()
    labelstyle1.configure("BW2.TLabel", foreground="red3",background="#bdc3c7", font=("Helvetica",10))
    # sub-def sensor name
    labelstyle2 = ttk.Style()
    labelstyle2.configure("BW3.TLabel",background="#bdc3c7", font=("Helvetica",10))
    # sub-def middle button
    buttonstyle=ttk.Style()
    buttonstyle.configure("But1.TButton", background="#27ae60", height=1, width=15)

    #Konfiguracja przycisków do obsługi stringów wysyłanych do STM32-F7
    sendlabel=ttk.Label(mainwindow, text="Sygnały sterujące:", style="BW.TLabel").grid(row=3, column=2)
    startbutton=ttk.Button(mainwindow,text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
    stopbutton=ttk.Button(mainwindow,text="Stop BLDC", style="But1.TButton").grid(row=6,column=2)
    testbutton=ttk.Button(mainwindow,text="Connection test", style="But1.TButton", command=testbutton_clicked).grid(row=7,column=2)

    #Konfiguracja przycisków przechodzenia do okienek od FFT
    Gaussianlabel=ttk.Label(mainwindow, text="Gaussian windows:", style="BW.TLabel").grid(row=3, column=0)
    sensor1button=tk.Button(mainwindow,text="Sensor 1 FFT", width=15, height=1).grid(row=5, column=0)
    sensor2button=tk.Button(mainwindow,text="Sensor 2 FFT", width=15, height=1).grid(row=6, column=0)
    sensor3button=tk.Button(mainwindow,text="Sensor 3 FFT", width=15, height=1).grid(row=7, column=0)

    #Konfiguracja wyświetlania pomiarów na żywo
    Sensorlabel=ttk.Label(mainwindow, text="Odczyt z sensorów:", style="BW.TLabel").grid(row=3, column=5,columnspan=2)
    sensor1lbl=ttk.Label(mainwindow,text="Sensor 1:", style="BW3.TLabel").grid(row=5, column=5)
    sensor2lbl=ttk.Label(mainwindow,text="Sensor 2:", style="BW3.TLabel").grid(row=6, column=5)
    sensor3lbl=ttk.Label(mainwindow,text="Sensor 3:", style="BW3.TLabel").grid(row=7, column=5)
    sensor4lbl=ttk.Label(mainwindow,text="Sensor 4:", style="BW3.TLabel").grid(row=8, column=5)
    sensor5lbl=ttk.Label(mainwindow,text="Sensor 5:", style="BW3.TLabel").grid(row=9, column=5)

    #radiobut do plota
    ttk.Label(mainwindow, text="Wybierz wartość do plota:", style="BW.TLabel").grid(row=10, column=2)
    comboExample = ttk.Combobox(mainwindow,values=["Sensor1","Sensor2","Sensor3","Sensor4"], width=10).grid(row=11, column=2)

    mainwindow.resizable(0, 0)
    while True:
        global data_int, i, fig, signal
        mainwindow.update_idletasks()
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
            rysuj_plot()
            if signal==1:
                canvas = FigureCanvasTkAgg(fig, master=mainwindow)  # A tk.DrawingArea.
                canvas.draw()
                canvas.get_tk_widget().grid(row=12, column=0, rowspan=2, columnspan=7)
        except socket.error: #jezeli socket nie dostaje danych:
            pass #zwolnienie programu w momencie, kiedy socket nie dostaje danych
def welcomewindowwidget():
    global entryIP, entryport, welcomewindow
    welcomewindow = tk.Tk()
    #Definicja stylu
    labelstyle = ttk.Style()
    labelstyle.configure("BW.TLabel", foreground="black",background="#bdc3c7", font=("Helvetica",10))
    labelstyle.configure("BW1.TLabel", foreground="black",background="#bdc3c7", font=("Helvetica",7))
    buttonstyle=ttk.Style()
    buttonstyle.configure("But1.TButton", background="#27ae60", height=1, width=15)
    welcomewindow.title("Praca inżynierska - stanowisko pomiarowe BLDC")
    welcomewindow.configure(bg="#bdc3c7")
    putlogo1=tk.PhotoImage(file="put.png")
    tk.Label(welcomewindow, image=putlogo1, background="#bdc3c7", relief="solid").grid(row=1, column=0, columnspan=2)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Automatyczne stanowisko pomiarowe \nwraz z analizą czasowo-częstotliwościową do badań \nwysokoobrotowych silników elektrycznych małych mocy.",justify = "center").grid(row=0, column=0, columnspan=2)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Skonfiguruj połączenie z STM32:").grid(row=2, column=0,columnspan=2)

    #Connection info + buttons
    ttk.Label(welcomewindow, style="BW.TLabel", text="Adres IP :").grid(row=3, column=0)
    ttk.Label(welcomewindow, style="BW.TLabel", text="Port :").grid(row=4, column=0)
    entryIP=ttk.Entry(welcomewindow)
    entryIP.grid(row=3, column=1)
    entryport=ttk.Entry(welcomewindow)
    entryport.grid(row=4,column=1)
    ttk.Button(welcomewindow,style="But1.TButton", text="connect",command=connectbutton_clicked).grid(row=5, column=0, columnspan=2)


    #Authors
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Autorzy pracy:").grid(row=6,column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Kamil Olszewski (133657)").grid(row=7, column=1, sticky="E")
    ttk.Label(welcomewindow, style="BW1.TLabel", text="Daniel Świątek (133671)").grid(row=8, column=1, sticky="E")

    welcomewindow.resizable(0,0)
    welcomewindow.mainloop()

welcomewindowwidget()

