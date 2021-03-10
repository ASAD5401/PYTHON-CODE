n=str(input()).split()
q=int(n[0])
w=int(n[1])
s1=str(input()).split()
l=list()
for i in range(q):
    l.append(int(s1[i]))
s2=str(input()).split()
t=list()
for i in range(w):
    t.append(int(s2[i]))
k=list()
for i in range(1,101):
    v=0
    for m in l:
        if i % m == 0:
            v+=1
    if v==len(l):
        k.append(i)
h=list()
for i in k:
    c=0
    for j in t:
        if j%i==0:
            c+=1
    if c==len(t):
        h.append(i)
print(len(h))