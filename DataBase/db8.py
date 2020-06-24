import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
#delete manually
conn.execute("DELETE from sa where NAME='SAHIL';")
conn.commit()
print("Data deleted ")
