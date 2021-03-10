parentslist=["asad","saad","saima","munawar","muzafar","shaheen","samreen"]
mylist=["saad","mubashir","hamza","asad","saima","ameen"]
f=set(parentslist)
c=set(mylist)
b=f.intersection(c)
e=len(b)
n=f.difference(b)
w=len(n)
s=c.difference(b)
q=len(s)
sum=e+w+q
print(sum)












