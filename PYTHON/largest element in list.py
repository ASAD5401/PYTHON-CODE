def max1(arr,s):
    m=arr[0]
    for x in range(s):
        if(arr[x]>m):
            m=arr[x]
    return m
l1=[45.56,62,1,4,98]
s=len(l1)
result=max1(l1,s)
print("The largest element in list is",result)
