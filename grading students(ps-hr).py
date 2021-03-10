from math import*
n=int(input())
for i in range(n):
    a=int(input())
    if a>37:
        q=a/5
        w=ceil(q)
        e=5*w
        r=e-a
        if(r<3):
            print(e)
        else:
            print(a)
    else:
        print(a)