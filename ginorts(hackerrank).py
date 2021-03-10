a="SortinGHg13678924"
l=list()
k=list()
j=list()
h=list()
for i in a:
    if(i.islower()):
       l.append(ord(i))
    elif(i.isupper()):
        k.append(ord(i))
    else:
        if(int(i)%2==0):
             h.append(ord(i))
        else:
            j.append(ord(i))
l.sort()
k.sort()
j.sort()
h.sort()
t=l+k+j+h
for i in t:
    print(chr(i),end="")