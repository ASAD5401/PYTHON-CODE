a=str(input()).split()
q=int(a[0])
w=int(a[1])
k=list()
j=list()
c=0
for i in range(q):
    d=str(input()).split()
    e=int(d[0])
    r=int(d[1])
    if r==1:
        k.append(e)
        c+=1
    elif r==0:
        j.append(e)
m=sum(j)
k.sort()
h=list()
if c>w:
    x=c-w
    for i in range(x):
        h.append(k[0])
        del(k[0])
v=sum(h)
p=sum(k)
print(p+m-v)
