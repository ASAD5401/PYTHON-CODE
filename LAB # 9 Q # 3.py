s=set({})
x=set({})
for i in range(3):
    a=input("Enter your best dishes:")
    s.add(a)
print(s)
for i in range(3):
    s.pop()
print(s)