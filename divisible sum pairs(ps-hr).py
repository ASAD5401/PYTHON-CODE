a=str(input()).split()
q=int(a[0])
w=int(a[1])
b=str(input()).split()
l=list()
for i in range(q):
    c=int(b[i])
    l.append(c)
p=0
for i in range(len(l)):
    for j in range(1,len(l)):
        c=l[i]+l[j]
        if i<j:
            if c%w==0:
                p+=1
print(p)