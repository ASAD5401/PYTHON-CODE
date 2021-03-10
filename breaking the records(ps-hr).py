q=int(input())
s=str(input()).split()
l=list()
for i in range(q):
    l.append(int(s[i]))
min=l[0]
max=l[0]
mi=0
ma=0
for i in l:
    if i>max:
        max=i
        ma+=1
    elif i<min:
        min=i
        mi+=1
print(ma,mi)

