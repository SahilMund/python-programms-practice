#inserting markdown button
from tkinter import *
from tkinter.ttk import *
windows=Tk()
windows.title("markdown Button GUi")
windows.geometry('350x200')
combo=Combobox(windows)
combo['values']=("Select",1,2,3,4,5)
#combo.current(0) sets the selected item
print(combo.get())
combo.place(x=10,y=50)
windows.mainloop()