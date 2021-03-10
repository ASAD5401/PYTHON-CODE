mychoiceofdishes={1:"biryani",2:"kofte",3:"palao",4:"burger",5:"pizza"}
cookeddishes={1:"karahi",2:"biryani",3:"daal",4:"bhindi",5:"karele",6:"burger"}
s1=set()
s2=set()
for x in mychoiceofdishes.values():
    s1.add(x)
for y in cookeddishes.values():
    s2.add(y)
com=s1.intersection(s2)
print("You will get",len(com),"dishes of your choice in this week.")
com=list(com)
print("The list of disheh are",com)