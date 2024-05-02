from tkinter import *
import datetime
from PIL import Image,ImageTk

root = Tk()
root.geometry("600x720")
root.title("Age Calculator App")
root.resizable(0,0)

name = Label(root,text="Name")
name.place(x=200,y=300)
year = Label(root,text="Year")
year.place(x=200,y=350)
month = Label(root,text="Month")
month.place(x=200,y=400)
day = Label(root,text="Day")
day.place(x=200,y=450)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root,textvariable=nameValue,width=25,font='Arial 14 bold')
nameEntry.place(x=250,y=300)
yearEntry = Entry(root,textvariable=yearValue,width=25,font='Arial 14 bold')
yearEntry.place(x=250,y=350)
monthEntry = Entry(root,textvariable=monthValue,width=25,font='Arial 14 bold')
monthEntry.place(x=250,y=400)
dayEntry = Entry(root,textvariable=dayValue,width=25,font='Arial 14 bold')
dayEntry.place(x=250,y=450)

def userInput():
    name = nameEntry.get()
    hero = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get())))
    textArea = Text(master=root,height=5,width=35,bg='pink',font='Arial 14 bold')
    textArea.place(x=200,y=550)
    answer = "Hello {hero} !!!. You are {age} years old ! , Don't Ask me Again !!".format(hero=name,age=hero.age())
    textArea.insert(END,answer)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age  

button = Button(root,text="Calculate Age",command=userInput,bg='red',font='Arial 16 bold')
button.place(x=300,y=500)

root.mainloop()