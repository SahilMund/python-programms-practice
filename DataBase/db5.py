import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
#select data from table
cursor=conn.execute("SELECT * from sa")
for row in cursor:
     print(row)
print("Operation done successfully")
