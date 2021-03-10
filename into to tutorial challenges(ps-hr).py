n=int(input())
m=int(input())
s=str(input()).split()
l=list()
for i in range(m):
    l.append(int(s[i]))
q=l.index(n)
print(q)