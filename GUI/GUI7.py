#inserting Radiobutton in GUI
from tkinter import *
from tkinter.ttk import *
windows=Tk()
windows.title("Radiobutton Button GUi")
selected=IntVar()
rad1= Radiobutton(windows,text='First',value=1,variable=selected)
rad2= Radiobutton(windows,text='Second',value=2,variable=selected)
rad3= Radiobutton(windows,text='Third',value=3,variable=selected)
def clicked():
    print(selected.get())
btn= Button(windows,text="click me",command=clicked)
rad1.place(x=100,y=50)
rad2.place(x=150,y=50)
rad3.place(x=200,y=50)
btn.place(x=250,y=50)
windows.mainloop()