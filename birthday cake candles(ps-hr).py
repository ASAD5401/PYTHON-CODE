n=int(input())
a=str(input()).split()
l=list()
for i in range(n):
    l.append(int(a[i]))
q=max(l)
e=l.count(q)
print(e)