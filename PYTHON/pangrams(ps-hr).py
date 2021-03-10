s=str(input())
p=s.casefold()
l=list()
for i in p:
    if i.isalpha():
        l.append(i)
q=set(l)
if len(q)==26:
    print("pangram")
else:
    print("not pangram")