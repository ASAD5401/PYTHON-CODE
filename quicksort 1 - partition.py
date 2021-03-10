n=int(input())
l=list()
s=str(input()).split()
for i in range(n):
    l.append(int(s[i]))
k=list()
j=list()
h=list()
for i in range(1,n):
    if l[i]>l[0]:
        k.append(l[i])
    elif l[i]<l[0]:
        j.append(l[i])
j.sort(reverse=True)
for i in j:
    h.append(str(i))
h.append(str(l[0]))
k.sort()
for i in k:
    h.append(str(i))
m=" ".join(h)
print(m)