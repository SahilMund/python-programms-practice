from tkinter import *
from tkinter import messagebox
def log():
    windows= Tk()
    windows.title("log-in portal")
    windows.geometry('350x200')
    lb1 = Label(windows, text="Enter Username:")
    lb1.place(x=100, y=50)
    user_id=Entry(windows,width=20)
    user_id.place(x=170, y=50)
    lb2 = Label(windows, text="Enter Password:")
    lb2.place(x=100, y=80)
    pwd=Entry(windows,width=20)
    pwd.place(x=170, y=80)
    def clicked():
        print(user_id.get())
        print(pwd.get())
        if user_id.get()=="Sahil" and pwd.get()=="1234500":
            windows.destroy()
            welcome()
        else:
            messagebox.showerror("Error Message ! Invalid password or username")
    btn=Button(windows, text="click",fg="red",bg="yellow",command=clicked)
    btn.place(x=200, y=140)
    windows.mainloop()
def welcome():
    windows = Tk()
    windows.title("welcome")
    windows.mainloop()
log()
