#connect with database
import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
print("Opened database succesfully")
