name = []
roll = []
marks = []
stream = []
for i in range(2):
    nm=input("Enter your name :")
    r=input("Enter ur roll np:")
    mk=int(input("Enter ur marks"))
    stm=input("Enter ur stream")
    name.append(nm)
    roll.append(r)
    marks.append(mk)
    stream.append(stm)
details=[]
print(name, roll,   marks,  stream)
details.append(name)
details.append(roll)
details.append(marks)
details.append(stream)
print(details)
t=max(marks)
i=marks.index(t)
print(t,i)