import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
#update data in sql
conn.execute("UPDATE sa  set STREAM= 'ELECTRONICS_CE'  where ID=1")
conn.commit()
