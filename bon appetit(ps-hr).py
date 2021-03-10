a=str(input()).split()
q=int(a[0])
w=int(a[1])
s=str(input()).split()
k=int(input())
l=list()
for i in range(q):
    c=int(s[i])
    l.append(c)
del(l[w])
v=sum(l)
f=v/2
if f==k:
    print("Bon Appetit")
else:
    print(int(k-f))
