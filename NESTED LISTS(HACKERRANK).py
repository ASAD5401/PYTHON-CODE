l=list()
for i in range(int(input())):
    k=list()
    name=str(input()).title()
    marks=eval(input())
    k.append(name)
    k.append(marks)
    l.append(k)
h=[j[1] for j in l]
m=min(h)
c=h.count(m)
for i in range(c):
    h.remove(m)
n=min(h)
z=h.count(n)
q=list()
for i in l:
    if i[1]==n:
        q.append(i[0])
w=sorted(q)
for i in w:
    print(i)