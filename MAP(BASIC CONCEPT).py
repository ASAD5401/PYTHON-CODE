a=[1,2,3,4,5,6,7,8,9,0]
def square(a):
    return a*a
b=map(square,a)
print(list(b))

name=["ASAD ALI KHAN","SAAD KHAN","NIMRA NAZ","SAIMA NAZ","UMAR WARSI","AFFAN WARSI"]
def lastname(name):
    ln=name.split(" ")[-1]
    return ln
last_name=print(list(map(lastname,name)))