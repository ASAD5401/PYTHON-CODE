import itertools
l=list()
k=list()
a=str(input()).split()
for i in a:
    l.append(int(i))
b=str(input()).split()
for i in b:
    k.append(int(i))
cart=itertools.product(l,k)
z=list(cart)
for i in z:
    print(i,end=" ")
