n=int(input())
s=str(input()).split()
l=list()
for i in range(len(s)):
    l.append(int(s[i]))
q=set(l)
p=list(q)
p.sort()
t=len(p)
print(p)
print(p[t-2])

