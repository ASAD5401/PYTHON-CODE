from math import*
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=0
while(n<=9):
    if(n==0 or n==1):
        print(n,"!","\t=","1")

    else:

        result=fact(n)
        print(n, "!", "\t=",result)
    n = n + 1