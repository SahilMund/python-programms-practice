a=int(input("enter a number :"))
b=a
rev=0
while b>0:
    r=b%10
    rev=rev*10+r
    b=int(b/10)

if(rev==a):
    print(a," is a palindrom number")
else:
    print(a," is not a pallindrom number")