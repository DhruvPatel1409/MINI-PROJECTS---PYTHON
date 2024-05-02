from tkinter import *
from translate import Translator

Screen = Tk()
Screen.title("LANGUAGE TRANSLATOR APP")
Screen.geometry("450x350")
Screen.resizable(0,0)
Screen.config(bg="lightblue")

InputLanguageChoice = StringVar()
InputLanguageChoice.set("English")
LanguageChoice = OptionMenu(Screen,InputLanguageChoice,'Hindi','French','Spanish','German','Spanish')
LanguageChoice.config(bg="white",fg="black")
LanguageChoice["menu"].config(bg="lightpink")
LanguageChoice.grid(row=2,column=2,pady=10,ipadx=15)

OutputLanguageChoice = StringVar()
OutputLanguageChoice.set("Choose here")
LanguageChoice = OptionMenu(Screen,OutputLanguageChoice,'Hindi','English','French','Spanish','German','Spanish')
LanguageChoice.config(bg="white",fg="black")
LanguageChoice["menu"].config(bg="lightpink")
LanguageChoice.grid(row=2,column=4,pady=10,ipadx=15)

Label(Screen,text="Enter text here").grid(row=3,column=1)
TextVar = StringVar()
Textbox = Entry(Screen,textvariable=TextVar).grid(row=3,column=2,ipadx=15,ipady=20)

Label(Screen,text="Output text").grid(row=3,column=3)
OutputVar = StringVar()
Textbox = Entry(Screen,textvariable=OutputVar).grid(row=3,column=4,ipadx=15,ipady=20)

def Translate():
    translator = Translator(from_lang=InputLanguageChoice.get(),to_lang=OutputLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

B = Button(Screen,text="translate",command=Translate,relief=GROOVE).grid(row=4,column=3)

Screen.mainloop()