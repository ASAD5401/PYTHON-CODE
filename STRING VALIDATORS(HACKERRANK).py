a=input()

for i in a:
    x="False"
    if(i.isalnum())==True:
        x="True"
        break
print(x)
for i in a:
    x="False"
    if(i.isalpha())==True:
        x="True"
        break
print(x)
for i in a:
    x="False"
    if(i.isnumeric()==True):
        x="True"
        break
print(x)
for i in a:
    x="False"
    if (i.islower()==True):
        x="True"
        break
print(x)
for i in a:
    x="False"
    if (i.isupper()==True):
        x="True"
        break
print(x)
