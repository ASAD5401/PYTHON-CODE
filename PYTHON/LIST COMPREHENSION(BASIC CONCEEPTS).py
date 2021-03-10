#list comprehension
b=[x for x in range(1,11)]
print(b)

b=[x if(x%2==0) else(x+1) for x in range(1,11)]
print(b)

b=[x for x in range(1,11) if (x > 2)]
print(b)