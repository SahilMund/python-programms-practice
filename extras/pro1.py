name=input("enter a name:")
count=0
for i in range(0,len(name)):
    if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u' or name[i]=='A' or  name[i]=='E' or name[i]=='I' or name[i]=='O' or name[i]=='U' :
        count+=1
        print('The vowels are : ',name[i])

print('total number of vowels present',count)
# reversing the string
print('the name in reverse order:')
for i in range(len(name)-1,-1,-1):
    print(name[i])
#replace vowels by x
print("replacing vowels by x")
for i in range(0,len(name)):
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u' or name[i] == 'A' or name[i] == 'E' or name[i] == 'I' or name[i] == 'O' or name[i] == 'U':
        name[i]="x"
    else:
        name[i]=i
print(name[i])





