n=int(input())
s=str(input()).split()
l=list()
for i in range(n):
    l.append(int(s[i]))
q=sum(l)
print(q)