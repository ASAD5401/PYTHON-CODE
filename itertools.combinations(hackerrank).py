import itertools
o=str(input()).split()
a=o[0]
l=list()
k=list()
for i in a:
    l.append(ord(i))
l.sort()
for i in l:
    k.append(chr(i))
w="".join(k)
b=int(o[1])+1
for f in range(1,b):
    m=itertools.combinations(w,f)
    p=list(m)
    for i in range(len(p)):
        x=p[i]
        for j in range(f):
            print(x[j],end="")
        print()