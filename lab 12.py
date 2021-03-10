import random
a=["Karachi","Lahore","Faislabad","Islamabad","Quetta","Multan"]
random.shuffle(a)
print(a)

import random
a=list()
l=["Asad","Saad","Ali","Ahmas","Ahsan","Tariq","Hassan"]
for i in range(len(l)):
    a.append(l.pop())
print(a)
a=random.sample(a,2)
print("The students who got scholarship are",a[0],"&",a[1]+".")

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

for i in range(5):
    a = random.choice(dice1)
    b = random.choice(dice2)
    print("Player 1 got:",a,"$",b)
    a = random.choice(dice1)
    b = random.choice(dice2)
    print("Player 2 got:", a, "$", b)