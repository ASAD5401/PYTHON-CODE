s=str(input()).split()
q=int(s[0])
w=int(s[1])
e=int(s[2])
a=str(input()).split()
z=int(a[0])
x=int(a[1])
c=int(a[2])
p=0
y=e-c
m=w-x
d=q-z
if(d>0 and m==0 and y==0):
    p=15*d
elif(m>0 and y==0):
    p=500*m
elif(y>0):
    p=10000*y
print(p)