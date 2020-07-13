import tkinter as tk
from tkinter import ttk

i=1
sensor1=1.3243
sensor2=1.3243
sensor3=1.3243

def startbutton_clicked():
    global i
    i+=1

#Definicja wyglądu mainwindow
mainwindow = tk.Tk()
mainwindow.configure(bg="#bdc3c7")
mainwindow.title("BLDC")
putlogo=tk.PhotoImage(file="put.png")
putlogolabel=tk.Label(mainwindow, image=putlogo, background="#bdc3c7", relief="solid").grid(row=1, column=2)
lbl = tk.Label(mainwindow,bg="#bdc3c7", text="Sterowanie hamownią silników BLDC - Nucelo F7", font=("Helvetica",16)).grid(row=0,column=2)
spacer=tk.Label(mainwindow, text="", bg="#bdc3c7").grid(row=2, column=2)
lbl2 =tk.Label(mainwindow,bg="#bdc3c7", text="Podłączono z sięcią \n Ethernet UDP \n Adres IP: 192.0.0.1 \n Port: 1234", relief="solid", font=("Arial",8)).grid(row=1, column=5, columnspan=2)

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
startbutton=ttk.Button(text="Start BLDC", style="But1.TButton", command=startbutton_clicked).grid(row=5,column=2)
stopbutton=ttk.Button(text="Stop BLDC", style="But1.TButton").grid(row=6,column=2)
fftbutton=ttk.Button(text="FFT", style="But1.TButton").grid(row=7,column=2)

#Konfiguracja przycisków przechodzenia do okienek od FFT
Gaussianlabel=ttk.Label(mainwindow, text="Gaussian windows:", style="BW.TLabel").grid(row=3, column=0)
sensor1button=tk.Button(text="Sensor 1 FFT", width=15, height=1).grid(row=5, column=0)
sensor2button=tk.Button(text="Sensor 2 FFT", width=15, height=1).grid(row=6, column=0)
sensor3button=tk.Button(text="Sensor 3 FFT", width=15, height=1).grid(row=7, column=0)

#Konfiguracja wyświetlania pomiarów na żywo
Sensorlabel=ttk.Label(mainwindow, text="Odczyt z sensorów:", style="BW.TLabel").grid(row=3, column=5,columnspan=2)
sensor1lbl=ttk.Label(text="Sensor 1:", style="BW3.TLabel").grid(row=5, column=5)
valuesens1=ttk.Label(text=str(sensor1) + " [rpm]", style="BW2.TLabel").grid(row=5,column=6)
sensor2lbl=ttk.Label(text="Sensor 2:", style="BW3.TLabel").grid(row=6, column=5)
valuesens2=ttk.Label(text=str(sensor2) + " [mA]", style="BW2.TLabel").grid(row=6,column=6)
sensor3lbl=ttk.Label(text="Sensor 3:", style="BW3.TLabel").grid(row=7, column=5)
valuesens3=ttk.Label(text=str(sensor3) + " [V]", style="BW2.TLabel").grid(row=7,column=6)
sensor4lbl=ttk.Label(text="Sensor 3:", style="BW3.TLabel").grid(row=8, column=5)
valuesens4=ttk.Label(text=str(sensor3) + " [V]", style="BW2.TLabel").grid(row=8,column=6)
sensor5lbl=ttk.Label(text="Sensor 3:", style="BW3.TLabel").grid(row=9, column=5)
valuesens5=ttk.Label(text=str(sensor3) + " [V]", style="BW2.TLabel").grid(row=9,column=6)


mainwindow.mainloop()