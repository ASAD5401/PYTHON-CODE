a=str(input()).split()
q=int(a[0])
w=int(a[1])
s=str(input()).split()
l=list()
for i in s:
    l.append(int(i))
l.sort()
k=list()
for i in l:
    if sum(k) < w:
        k.append(i)
        if sum(k)>w:
            k.remove(i)
            break
print(len(k))
