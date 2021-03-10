import os
f=open("d:\\asad.txt","r")
q=f.read()
f.close()
w=q.split()
print(w)
o=len(w)
c=0
for i in w:
    for j in w:
        if i.lower() == j.lower():
            c+=1
if(c>o):
    print("duplicate words are present")
else:
    print("duplicate words are not present")