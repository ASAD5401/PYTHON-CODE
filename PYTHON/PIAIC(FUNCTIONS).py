#positional and keyword arguments
def add(a,b,c):
    print(a+b+c)
add(4,6,c=9)
#add(a=9,7,2)
#add(2,3,a=8)

#default arguments
#default argument is middle
def name(first,last,middle=" Ali"):
    print(first,middle,last)
name("Asad","Khan")
name("saad","ali","khan")

#unknown arguments
def pizza(*toppings,flavour,size):
    toppings=[i for i in toppings]
    if len(toppings)>1:
        toppings.insert(len(toppings)-1,"and")

    a=" ".join(toppings)
    print(f"Your pizza of size {size} with flavour {flavour} and toppings of {a} is ready.")
pizza("Medium","lkj,flavour="Fajita",size="Mushrooms")

#return
def add(a,b):
    c=a+b
    d=a-b
    return c,d
print(add(10,4))
z=add(10,4)
print(z)
m,n=add(10,4)
print(m,n)
print(f"the addition is {m} and subtraction is {n}")
print(m, "&", n)
# most important
print(m & n)
print()

#using functions as variables
#yahan pe phle call sub ko jai ge wh execute hoga phr add ke pas jai ga interpreter
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
result=add(10,4)+sub(10,4)
print(result)

#local vs global
def a():
    name="asad"
    print(name)
a()
print(name)
name="sas"
def b():
    print(name)
b()
print()

#functions with in function

def salary(basic,sales):
    print(basic+comm(sales))
def comm(sales):
    if sales>100:
        return sales*100
    elif(sales>50):
        return sales*50
    else:
        return 0
salary(20000,111)