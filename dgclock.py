from tkinter import *
from time import strftime

root = Tk()
root.title("DIGITAL CLOCK")

def time():
    timeFormat = strftime('%I:%M:%S %p')
    clock.config(text=timeFormat)
    clock.after(1000, time)

clock = Label(root, font="Arial 100 bold", pady=30, fg="cyan", bg="black")
clock.pack(anchor="center")
time()
mainloop()
