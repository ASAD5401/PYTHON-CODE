c=0
n=int(input("no:"))
if(n==1):
    print("composite")
else:
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        print("no is prime")
    else:
        print("no is not prime")

