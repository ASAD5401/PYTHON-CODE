n=int(input())
for i in range(n):
    a=int(input())
    b = 1
    for j in range(1,a+1):
        if(j%2==0):
            b+=1
        else:
            b=b+b
    print(b)
