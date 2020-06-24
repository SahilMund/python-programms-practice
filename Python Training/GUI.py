from tkinter import *
#create simple GUI window
'''windows = Tk()
windows.title("GUI IN PYTHON")
windows.mainloop()
#print text on GUI
windows=Tk()
windows.title("print Text")
#lbl=Label(windows,text="Hello TK")
lbl=Label(windows,text="Hello TK",font=("Times New Roman Bold",50))
#lbl.grid(column=0,row=0)
lbl.place(x=50,y=30)##to change the position of the text
windows.mainloop()'''

#Add a Click Button
'''windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Hello")
lbl.place(x=20,y=30)
btn=Button(windows,text="Click",fg="white", bg="blue")
btn.place(x=40,y=50)
windows.mainloop()'''


#configure a Button:
'''windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Hello")
lbl.place(x=30,y=20)
def clicked():
    lbl.configure(text="Button Clicked")
btn=Button(windows,text="Click", command=clicked)
btn.place(x=30,y=40)
windows.mainloop()'''


#validation:
'''windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Enter name")
lbl.place(x=30,y=20)
ent=Entry(windows,width=20)
ent.place(x=50,y=80)
def clicked():
     lbl.configure(text="Thank u")
     print(ent.get())
btn=Button(windows,text="Click", command=clicked)
btn.place(x=30,y=40)
windows.mainloop()'''


#program-1:
#create a username & pw  and validation of it
'''windows= Tk()
windows.title("FORM")
windows.geometry('400x300')
windows.geometry('400x300')
lbl=Label(windows,text="Username")
lbl1=Label(windows,text="Password")
lbl.place(x=40,y=40)
lbl1.place(x=40,y=60)
ent=Entry(windows,width=20)
ent1=Entry(windows,width=20)
ent.place(x=120,y=40)
ent1.place(x=120,y=60)
def clicked():
    lbl.configure(text="verified")
    print(ent.get())
    print(ent1.get())
btn=Button(windows,text="Done", command=clicked)
btn.place(x=70,y=90)
windows.mainloop()'''
                 
                 
                 




#to create a dropdown:/Combobox in GUI:

'''from tkinter.ttk import * #to define combobox we have to use this..
windows= Tk()
windows.title("Markdown Button GUI")
windows.geometry('350x200')
combo = Combobox(windows)
combo['values']= ("Select",1,2,3,4,5)
#combo.current(0) #set the selected item
print(combo.get())
combo.place(x=20,y=40)
windows.mainloop()'''


#Create a RadioButton:(INCOMPLETE)

'''from tkinter.ttk import *
windows=Tk()
windows.title("Receive value Radio GUI")
windows.geometry('350x200')
selected = IntVar()
rad1 = Radiobutton(windows,text='First',value=1,variable=selected)
rad2 = Radiobutton(windows,text='Second',value=2,variable=selected)
rad3 = Radiobutton(windows,text='Third',value=3,variable=selected)
def clicked():
    print(selected.get())
btn=Button(windows,text="Click me",command=clicked)'''


#

'''from tkinter import *
def w1():
    windows=Tk()
    windows.title("My First GUI In Python")
    lbl=Label(windows,text="widget-1",font=("Times New Roman Bold",30))
    lbl.place(x=20,y=40)
    def clicked():
        windows.destroy()
        w2()
btn=Button(windows,text="click",command=clicked)
btn.place(x=40,y=70)
windows.mainloop()
def w2():
    
    windows=Tk()
    windows.title("My First GUI In Python")
    lbl=Label(windows,text="widget-1",font=("Times New Roman Bold",30))
    lbl.place(x=20,y=40)
    def clicked():
        windows.destroy()
        w1()
btn=Button(windows,text="click",command=clicked)
btn.place(x=40,y=70)
windows.mainloop()
    
    



from tkinter.ttk import *
windows=Tk()
windows.title("Receive value Radio GUI")
windows.geometry('350x200')
def clicked():
    Messagebox.showinfo('Message Title','Welcome to TK Message Box')
Messagebox.showwarning('Message title','Warning!')
Messagebox.showerror('Message Title', 'Opening error!')
res= Messagebox.askquestion('Message title','Question Box')
res= Messagebox.askretrycancel('Message title','Retry?')
btn= Button(windows,text='Click here', command=clicked)
btn.place(x=30,y=60)
windows.mainloop()
    

from tkinter import *
#create simple GUI window
windows = Tk()
windows.title("GUI IN PYTHON")
windows.mainloop()

#print text on GUI
windows=Tk()
windows.title("print Text")
#lbl=Label(windows,text="Hello TK")
lbl=Label(windows,text="Hello TK",font=("Times New Roman Bold",50))
#lbl.grid(column=0,row=0)
lbl.place(x=50,y=30)##to change the position of the text
windows.mainloop()

#Add a Click Button
windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Hello")
lbl.place(x=20,y=30)
btn=Button(windows,text="Click",fg="white", bg="blue")
btn.place(x=40,y=50)
windows.mainloop()


#configure a Button:
windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Hello")
lbl.place(x=30,y=20)
def clicked():
    lbl.configure(text="Button Clicked")
btn=Button(windows,text="Click", command=clicked)
btn.place(x=30,y=40)
windows.mainloop()



windows= Tk()
windows.title("print Text")
windows.geometry('350x200')
lbl=Label(windows,text="Enter name")
lbl.place(x=30,y=20)
ent=Entry(windows,width=20)
ent.place(x=50,y=80)
def clicked():
     lbl.configure(text="Thank u")
     print(ent.get())
btn=Button(windows,text="Click", command=clicked)
btn.place(x=30,y=40)
windows.mainloop()

    
'''
