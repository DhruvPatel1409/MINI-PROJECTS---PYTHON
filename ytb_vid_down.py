from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("600x350")
root.resizable(0,0)
root.config(bg="pink")
root.title("YOU TUBE VIDEO DOWNLOADER")

Label(root,text="Download any YouTube videos for free !!",font="Arial 14 bold").place(x=100,y=20)
Label(root,text="Paste your link here",font="Arial 14 bold",bg="pink").place(x=120,y=50)

videoLink = StringVar()
Entry(root,width=80,textvariable=videoLink).place(x=35,y=85)

def downloadVideo():
    url = YouTube(str(videoLink.get()))
    videoStream = url.streams.first()
    videoStream.download("C:/Users/ADMIN/Desktop/python jupyter/PROJECTS/mini projects")
    Label(root,text="Download Completed Successfully",font="Arial 14",bg="green",fg='white').place(x=120,y=180)

Button(root,text="Download Now",font="Arial 16 bold",bg='red',padx=2,command=downloadVideo).place(x=180,y=120)

root.mainloop()