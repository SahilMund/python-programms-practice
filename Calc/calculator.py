from ad_sb import addition,subs
from mlti import mul
from xpo import Exponential
from xpo.sqr import square
import div

x=eval(input("enter a no:"))
y=eval(input("enter another no:"))
calc=int(input("Enter Ur Choices:\n 1=addition \n 2=substraction \n 3=multiplication \n 4=division \n 5=exponential \n 6=square \n"))

if calc==1:
    a = addition.add(x, y)
    print("addition is :",a)
elif calc==2:
    s = subs.sub(x, y)
    print("substraction is :",s)
elif calc==3:
    m = mul.multi(x, y)
    print("multiplication is :",m)
elif calc==4:
    d = div.division(x, y)
    print("division is",d)
elif calc==5:
    x = Exponential.expo(x, y)
    print("exponential is:",x)
else:
    sq = square.sq(x)
    print("square is :",sq)















