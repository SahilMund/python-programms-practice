from tkinter import *
from tkinter.ttk import *
import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
cur=conn.execute("select roll from monday")
#roll=['values','Roll NO.','17ECE001','17ECE002','17ECE003','17ECE004','17ECE005','17ECE006','17ECE007','17ECE008','17ECE009','17ECE010']
roll=['select']
for row in cur:
     roll.append(row[0])
combo['values']=roll

