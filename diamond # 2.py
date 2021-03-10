n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1)+"*"*i)
for j in range(n-1,0,-1):
    print(" "*(n-j)+"*"*(j)+"*"*(j-1))