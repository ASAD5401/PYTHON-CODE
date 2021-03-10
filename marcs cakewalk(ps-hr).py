n=int(input())
s=str(input()).split()
l=list()
for i in range(n):
    l.append(int(s[i]))
l.sort(reverse=True)
k=list()
for i in range(n):
    m=(l[i])*(2**i)
    k.append(m)
print(sum(k))