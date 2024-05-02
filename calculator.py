from tkinter import *
root=Tk()
root.geometry("350x500")
root.resizable(0,0)
root.title('CALCULATOR')

def disp(number):
    global num
    num=num+str(number)
    label1['text']=num

def clear():
    global num
    num=''
    label1['text']=num

def evaluate():
    global num
    result=str(eval(num))
    label1['text']=result
    num=''

num=''
var=StringVar()

frame1=Frame(root)
frame1.pack(expand=TRUE,fill=BOTH)

frame2=Frame(root)
frame2.pack(expand=TRUE,fill=BOTH)

frame3=Frame(root)
frame3.pack(expand=TRUE,fill=BOTH)

frame4=Frame(root)
frame4.pack(expand=TRUE,fill=BOTH)

label1=Label(frame1,textvariable='',font=('Arial',20),anchor=SE,bg="white",fg="black")
label1.pack(expand=TRUE,fill=BOTH)

key1=Button(frame1,text="1",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(1))
key1.pack(expand=TRUE,fill=BOTH,side=LEFT)

key2=Button(frame1,text="2",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(2))
key2.pack(expand=TRUE,fill=BOTH,side=LEFT)

key3=Button(frame1,text="3",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(3))
key3.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_addition=Button(frame1,text="+",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp("+"))
key_addition.pack(expand=TRUE,fill=BOTH,side=LEFT)

key4=Button(frame2,text="4",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(4))
key4.pack(expand=TRUE,fill=BOTH,side=LEFT)

key5=Button(frame2,text="5",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(5))
key5.pack(expand=TRUE,fill=BOTH,side=LEFT)

key6=Button(frame2,text="6",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(6))
key6.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_subtraction=Button(frame2,text="-",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp("-"))
key_subtraction.pack(expand=TRUE,fill=BOTH,side=LEFT)

key7=Button(frame3,text="7",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(7))
key7.pack(expand=TRUE,fill=BOTH,side=LEFT)

key8=Button(frame3,text="8",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(8))
key8.pack(expand=TRUE,fill=BOTH,side=LEFT)

key9=Button(frame3,text="9",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(9))
key9.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_multiplication=Button(frame3,text="*",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp("*"))
key_multiplication.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_clear=Button(frame4,text="C",font=('Arial',20),border=0,bg="black",fg="white",command=clear)
key_clear.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_0=Button(frame4,text="0",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp(0))
key_0.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_equal=Button(frame4,text="=",font=('Arial',20),border=0,bg="black",fg="white",command=evaluate)
key_equal.pack(expand=TRUE,fill=BOTH,side=LEFT)

key_division=Button(frame4,text="/",font=('Arial',20),border=0,bg="black",fg="white",command=lambda:disp("/"))
key_division.pack(expand=TRUE,fill=BOTH,side=LEFT)

root.mainloop()