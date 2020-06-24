password="1234qwerty"
for i in range(4):
     pd=input("enter the password:  ")
     k=4
     if(pd==password):
          print("welcome ur really smart")
          print("u got points",i*10)
          break
     else:
          print("fuck off man!  u enterd the wrong password \nchances left",k-i)
          continue
          print("Try next tym")
          
