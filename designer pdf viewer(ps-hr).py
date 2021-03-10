a=str(input()).split()
l=list()
for i in range(26):
    l.append(int(a[i]))
k=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
f=str(input())
o=list()
for i in f:
    z=k.index(i)
    v=l[z]
    o.append(v)
i=max(o)
c=i*len(f)
print(c)