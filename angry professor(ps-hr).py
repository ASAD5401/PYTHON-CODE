n=int(input())
for i in range(n):
    a=str(input()).split()
    q=int(a[0])
    w=int(a[1])
    s=str(input()).split()
    l=list()
    for j in range(q):
        l.append(int(s[j]))
    k=list()
    for j in l:
        if j<=0:
            k.append(j)
    if(len(k)>=w):
        print("NO")
    else:
        print("YES")

