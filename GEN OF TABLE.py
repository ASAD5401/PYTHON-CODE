a=eval(input("Enter no of rows:"))
c=eval(input("Enter starting  point"))
d=eval(input("Enter ending point:"))
for i in  range(1,a+1):
    for j in range(c,d+1):
        print(i*j,end="\t")
    print()









row=eval(input("Enter number of rows:"))
col=eval(input("Enter number of columns:"))
for i in range(0,row):
    for j in range(0,col):
         print(i,end="")
    print()