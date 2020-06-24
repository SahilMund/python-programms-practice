from tkinter import *
from tkinter.ttk import *
def w1():
    windows= Tk()
    windows.title("Widget-2")
    windows.geometry('350x200')
    lb1 = Label(windows, text="widget-2")
    lb1.place(x=100, y=50)
    def clicked():
        windows.destroy()
        w2()
    btn = Button(windows, text="click", command=clicked)
    btn.place(x=200,y=50)
    windows.mainloop()
def w2():
    windows= Tk()
    windows.title("Widget-1")
    windows.geometry('350x200')
    lb1 = Label(windows, text="widget-1")
    lb1.place(x=100, y=50)
    def clicked():
        windows.destroy()
        w1()
    btn = Button(windows, text="click", command=clicked)
    btn.place(x=200,y=50)
    windows.mainloop()
w2()