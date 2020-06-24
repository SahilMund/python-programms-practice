from tkinter import *
#inserting a button
windows=Tk()
windows.title("Print text")
windows.geometry('350x200')
lb1=Label(windows,text="Hello Tk",font=("Times New Roman Bold",5))
lb1.place(x=100,y=50)
btn=Button(windows,text="click",fg="red",bg="yellow")
btn.place(x=200,y=50)
windows.mainloop()