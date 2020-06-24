i=0
j=0
x=int(input("multiplication table UPTO::"))
for i in range (1,x+1):
    for j in range (1,11):
        f = open("C:/Users/Sahil/Desktop/pro1/multi_table.txt", "a+")
        mul=i*j
        f.write("{} * {} = {} \n".format(i, j, mul))
f.close()
f = open("C:/Users/Sahil/Desktop/pro1/multi_table.txt", "r+")
content=f.read()
print("total characters present:",len(content))
print("The no. of * symbols are:", content.count('*'))
print("The number of = symbols are:", content.count('='))
f.close()