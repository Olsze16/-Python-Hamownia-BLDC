from tkinter import ttk
def welcomnewindowstyle():
    labelstyle = ttk.Style()
    labelstyle.configure("BW.TLabel", foreground="black",background="#bdc3c7", font=("Helvetica",10))
    labelstyle.configure("BW1.TLabel", foreground="black", background="#bdc3c7", font=("Helvetica", 7))
    buttonstyle=ttk.Style()
    buttonstyle.configure("But1.TButton", background="#27ae60", height=1, width=15)
def mainwindowstyle():
    labelstyle = ttk.Style()
    labelstyle.configure("BW.TLabel", foreground="black",background="#bdc3c7", font=("Helvetica",11))
    labelstyle.configure("BW1.TLabel", foreground="black", background="#bdc3c7", font=("Helvetica", 7))
    labelstyle.configure("BW2.TLabel", foreground="red3",background="#bdc3c7", font=("Helvetica",10))
    labelstyle.configure("BW4.TLabel", foreground="black", background="#bdc3c7", font=("Helvetica", 9))
    labelstyle.configure("BW3.TLabel",background="#bdc3c7", font=("Helvetica",10))
    # sub-def middle button
    buttonstyle=ttk.Style()
    buttonstyle.configure("But1.TButton", background="#27ae60", height=1, width=15)
    buttonstyle.configure("But2.TButton", background="blue", height=0.5, width=15)
    buttonstyle.configure("But3.TButton", background="#ffbb33", height=1, width=15)
    checkbuttonstyle=ttk.Style()
    checkbuttonstyle.configure("C1.TCheckbutton", background="bdc3c7", font=("Helvetica",10), width=15, height=1)