from tkinter import *
from tkcalendar import Calendar

app = Tk()
app.geometry("420x420")
app.title("Calendar Date Picker App")
app.config(bg="darkorange")

calendarObj = Calendar(app, selectmode="day", year=2024, month=1, date=1)
calendarObj.pack(pady=45)

date = Label(app, text="", bg="black", fg="white")
date.pack()

def fetch_date():
    date.config(text="Selected date is: " + calendarObj.get_date())

button = Button(app, text="Select Date", bg="black", fg="white", command=fetch_date)
button.pack()

app.mainloop()
