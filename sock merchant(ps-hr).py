from math import*
n=int(input())
a=str(input()).split()
l=list()
for i in range(n):
    c=int(a[i])
    l.append(c)
q=0
a=set(l)
s=list(a)
for i in s:
    p=l.count(i)
    if(p>1):
        q+=floor(p/2)
print(q)