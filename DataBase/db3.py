#create table using user  dafined name
import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
print("Opened database succesfully")
TABLE=input("Enter a Table name:")
conn.execute('''CREATE TABLE '''+TABLE+'''
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
          NAME          TEXT       NOT NULL,
          GRADE         INT         NOT NULL,
          ADDRESS       CHAR(50),
          STREAM        CHAR(50));''')
print("Table Created")

