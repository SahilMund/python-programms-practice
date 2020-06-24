from tkinter import *
#customise the button
windows=Tk()
windows.title("Print text")
windows.geometry('350x200')
lb1=Label(windows,text="Hello Tk")
def clicked():
    lb1.configure(text="Button Clicked")
lb1.place(x=100,y=50)
btn=Button(windows,text="click",fg="red",bg="yellow",command=clicked)
btn.place(x=200,y=50)
windows.mainloop()
