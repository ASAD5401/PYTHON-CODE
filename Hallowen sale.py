s=str(input()).split()
p=int(s[0])
d=int(s[1])
m=int(s[2])
z=m
s=int(s[3])
l=list()
if p<s:
    for i in range(p,z,-d):
        l.append(i)
    x=sum(l)
    a=len(l)
    while(x<s):
        x+=m
        a+=1
        if x>s:
            a-=1
            x-=6
            break
    print(a)
else:
    print(0)