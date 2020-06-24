import sqlite3
link="E:/Database/"
conn=sqlite3.connect(link+'StudentData.db')
#update by user preference
nameupd=input("Enter name to update:")
strmupd=input("Enter the stream name:")
conn.execute("UPDATE sa SET  STREAM= '"+strmupd+"' WHERE NAME= '"+nameupd+"'")
conn.commit()
