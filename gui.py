from tkinter import filedialog
from tkinter import *
import socket


# get IP Adress and Hostname
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)   

root = Tk(className="TakYoo Diashow")  
root.geometry("400x300+200+50")

def say_hi():
    root.directory =  filedialog.askdirectory(initialdir = "/users",title = "Ordner für Diashow ausaehlen")
    from move import exceMove
    exceMove(root.directory)
    print (root.directory)

def body(master):
    frame = Frame(master)
    frame.pack()

    Label(root, wraplength=300 ,text="Die Diashow ist ueber folgende Adresse im gleichen Netzwerk erreichbar: ").pack()

    var = StringVar()
    var.set(hostname)
    Label(root, textvariable = var).pack()

    Label(root, text="oder").pack()

    var = StringVar()
    var.set(IPAddr)
    Label(root, textvariable = var).pack()
    
    
    Button(frame, text="Programm beenden", fg="red", command=frame.quit).pack(side=LEFT)
    Button(frame, text="Ordner auswaehlen", command= lambda: say_hi()).pack(side=LEFT)

body(root)
root.mainloop()
