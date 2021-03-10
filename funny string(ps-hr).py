n=int(input())
for i in range(n):
    a=str(input())
    z=a[::-1]
    l=list()
    k=list()
    for i in a:
        l.append(ord(i))
    for i in z:
        k.append(ord(i))
    j=list()
    h=list()
    for i in range(len(a)-1):
        a=l[i]
        b=l[i+1]
        c=abs(a-b)
        j.append(c)
        d=k[i]
        e=k[i+1]
        f=abs(d-e)
        h.append(f)
    if h==j:
        print("Funny")
    else:
        print("Not Funny")