l1=[45,56,62,1,4,98]
print(l1)
n=len(l1)
for i in range(0,n):
    for j in range(1+i,n):
        if(l1[i]>l1[j]):
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
print(l1)