

b=str(input()).split()

s=set(b)

n=str(input()).split()

d=set(n)
q=s.difference(d)
w=d.difference(s)
e=q.union(w)
print(e)
r=list(e)
r.sort()
for i in r:
    print(i)
