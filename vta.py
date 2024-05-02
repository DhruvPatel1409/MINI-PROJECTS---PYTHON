from tkinter import font
import moviepy.editor as mp
from tkinter import *
from  tkinter import filedialog

def convert():
    videoClip = mp.VideoFileClip(fname)
    videoClip.audio.write_audiofile("sample.mp4")
    messageToGenerate.set("CONGRATULATIONS , AUDIO FILE IS GENERATED SUCCESSFULLY !!")

def upload():
    filename = filedialog.askopenfilename(filetypes=[('Mp4 Files','*.mp4'),('WMV Files','*.wmv'),('ogg files','*.ogg')])
    messageForUpload.set("FILE UPLOADED : "+filename)
    global fname
    fname = filename

root = Tk()
root.geometry("700x250")
root["bg"] = "pink"
root.title("VIDEO TO AUDIO CONVERTERING APP")

global messageForUpload
global messageToGenerate
messageForUpload = StringVar()
messageToGenerate = StringVar()

Label(root,text="sample",textvar=messageForUpload,font="Arial 12",fg='#fff').place(x=100,y=40)
Button(root,text="Upload Video",command=upload,font="Arial 12 bold",fg='#fff',bg='green').place(x=100,y=70)
Button(root,text="Convert Video",command=convert,font="Arial 12 bold",fg='#fff',bg='green').place(x=350,y=70)
Label(root,text="sample",textvar=messageToGenerate,font="Arial 12",fg='#fff').place(x=100,y=120)

root.mainloop()

