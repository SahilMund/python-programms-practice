from tkinter import *
#getting input from user
windows=Tk()
windows.title("Print text")
windows.geometry('350x200')
lb1=Label(windows,text="Enter name:")
lb1.place(x=100,y=50)
ent=Entry(windows,width=20)
ent.place(x=170,y=50)
def clicked():
    lb1.configure(text="Thank You")
    print(ent.get())
btn=Button(windows,text="click",fg="red",bg="yellow",command=clicked)
btn.place(x=200,y=80)
windows.mainloop()