n=int(input())
s=str(input()).split()
q1=set(s)
print(q1)
m=int(input())
b=str(input()).split()
w=set(b)
print(w)
e=q1.union(w)
print(e)
print(len(e))