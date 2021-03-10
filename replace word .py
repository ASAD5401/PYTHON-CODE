import os
w=open("d:\\ALI.txt","r+")
a=w.read()
w.close()
b=a.split()
print(b)
c=""
for i in b:

    if(len(i)==4):
        c+="xxxx "
    else:
        c+=i+" "
w=open("d:\\ALI.txt","r+")
q=w.write(c)
print(c)