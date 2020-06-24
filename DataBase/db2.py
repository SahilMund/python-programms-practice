#create a database and inside it create a table
import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
print("Opened database succesfully")
conn.execute('''CREATE TABLE STUDENTDATA
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
          NAME          TEXT       NOT NULL,
          GRADE         INT         NOT NULL,
          ADDRESS       CHAR(50),
          STREAM        CHAR(50));''')
print("Table Created")
