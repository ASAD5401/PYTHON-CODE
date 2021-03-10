
def vowel(x):
       if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
               print("letter is vowel")
       else:
             print("letter is not vowel")
x=input("enter any alphabet to check:")
result=vowel(x)
y=input("Did you want to check more alphabets?")
while(y=="yes"):
    x = input("enter any alphabet to check:")
    result=vowel(x)
    y = input("Did you want to check more alphabets?")