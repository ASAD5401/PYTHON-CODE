from math import*
def fact(x):
        fact=1
        for i in range(1,x+1):
                fact=fact*i
        return fact
x=0
while(x<=10):
    c=fact(x)
    print(x,"!\t=",c)
    x = x + 1