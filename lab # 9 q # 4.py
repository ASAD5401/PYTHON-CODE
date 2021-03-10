s={"bat":1000,"ball":300,"hellmet":800,"pads":2000,"shoes":500,"jersey":1500,"stumps":1000}
l1=list(s.values())
tamount=sum(l1)
v=int(input("Enter how many items do you want to buy? :"))
for i in range(v):
    m=input("Enter items you want to buy:")
    del s[m]
l2=list(s.values())
iamount=sum(l2)
bamount=(tamount-iamount)
print("The total amount of items that you buy is  :",bamount)
q=set(l1)
w=set(l2)
e=q.difference(w)
r=list(e)
r.sort()
print("The minimum amount of item that you buy is :",r[0])
r.sort(reverse=True)
print("The maximum amount of item that you buy is :",r[0])