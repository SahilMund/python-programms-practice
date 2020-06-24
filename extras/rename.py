a=eval(input("enter a no:"))
b=eval(input("enter another no :"))
c=a+b

f=open("C:/Users/Sahil/Desktop/pro1/add_res","w+")
f.write("addition of"+str(a)+"and"+str(b)+"is"+str(c))
f.close()
