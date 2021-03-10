n=int(input())
a=list()
for i in range(n):
    s=str(input()).split()
    l=list()
    for j in s:
        l.append(int(j))
    a.append(l)
l=list()
for i in range(n):
    z=a[i]
    l.append(z[i])
k=list()
for i in range(n,0,-1):
    x=a[i-1]
    k.append(x[n-i])
m=sum(k)
n=sum(l)
p=abs(m-n)
print(p)