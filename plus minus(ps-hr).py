n=int(input())
s=str(input()).split()
l=list()
k=list()
j=list()
for i in s:
    c=int(i)
    if c>0:
        l.append(i)
    if c==0:
        k.append(i)
    if c<0:
        j.append(i)
q=len(l)/n
w=len(j)/n
e=len(k)/n
print("{0:.6f}".format(q))
print("{0:.6f}".format(w))
print("{0:.6f}".format(e))