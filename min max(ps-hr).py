s=str(input()).split()
l=list()
for i in s:
    c=int(i)
    l.append(c)
l.sort()
q=l[0]
w=l[len(l)-1]
print(sum(l)-w,sum(l)-q)

