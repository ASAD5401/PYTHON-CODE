s=str(input()).split()
q=int(s[0])
w=int(s[1])
a=str(input()).split()
l=list()
for i in range(q):
    l.append(int(a[i]))
for i in range(w):
    d=str(input()).split()
    e=int(d[0])
    r=int(d[1])
    k=list()
    for i in range(e,r+1):
        k.append(l[i])
    print(min(k))