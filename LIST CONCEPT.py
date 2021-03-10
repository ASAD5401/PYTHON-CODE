
l1=[37,93,45,29,10,78,54,56,43,55]
x=len(l1)
y=int((x)/2)
print(y)
print(l1[y])
l1.sort(reverse=True)
print(l1)
l1=[37,93,45,29,10,78,54,56,43,55]
print("\n")
l1.append(l1[0])
del(l1[0])
print(l1)

l3=[1,2,33,4,35,6,7,8]
l3.append(10)
print(l3)
l3.insert(9,20)
print(l3)
l3.reverse()
print(l3)
for i in range(100):
    if(i<50):
        pass
    else:
        print(i)