l=[]
n=int(input("Enter no of elements in a array:"))
for i in range(n):
    a=int(input("Enter array elements:"))
    if(0<a and a<=1000):
         l.append(a)
sum=sum(l)
print(sum)
