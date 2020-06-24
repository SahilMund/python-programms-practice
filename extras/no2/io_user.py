def inp():
    x=int(input("Enter no of students:"))
    for i in range(x):
        nm=input("Enter the name:")
        file=open("E:/no2",'a+')
        file.write(nm +'\n')
        file.close()
def cnt():
    file = open("E:/no2", 'r+')
    x=file.read()
    print(x)
    print("no of characters are",len(x))



