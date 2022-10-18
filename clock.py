from tkinter import *
from tkinter.ttk import *
from time import strftime

base=Tk()
base.title("clock")

def gettime():
    present=strftime('%H:%M:%S %p')
    label.config(text=present)
    label.after(1000,gettime)

label=Label(base,font=("bold",80),background="black",foreground="cyan")
label.pack(anchor="center")
gettime()

mainloop()