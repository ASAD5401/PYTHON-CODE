def max1(arr,size):
    m=arr[0]
    for x in range(size):
        if(arr[x]>m):
            m=arr[x]
    return m
l1=[1,56,45,34,90]
size=len(l1)
print("the largest element in list is",max1(l1,size))