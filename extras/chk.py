'''str1=input()
if str1.isalnum()==False:
print("String contains special chars")'''

s=input("enter a string:")
c=0
d=0
e=0
i=0
for i in s:
    if i.isalnum() == False:
        c += 1
    elif i.isalpha() == True:
        d += 1
    elif i.isdigit() == True:
        e += 1
print("the no of special characters are:",c)
print("the no of alphabets are:",d)
print("The no of digits are:",e)