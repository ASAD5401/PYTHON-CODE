from math import*
name=input("Enter your name:")
fname=input("Enter your father's name:")
rno=input("Enter your roll number:")
s1=input("Enter subject name:")
m1=int(input("Enter marks:"))
s2=input("Enter subject name:")
m2=int(input("Enter marks:"))
s3=input("Enter subject name:")
m3=int(input("Enter marks:"))
s4=input("Enter subject name:")
m4=int(input("Enter marks:"))
s5=input("Enter subject name:")
m5=int(input("Enter marks:"))
omarks=m1+m2+m3+m4+m5
per=(omarks/500)*100
if(per>=80 and per<=100):
    grade="A-One"
elif(per>=70 and per<80):
    grade="A"
elif(per>=60 and per<70):
    grade="B"
elif(per>=50 and per<60):
    grade="C"
elif(per>=40 and per<50):
    grade="D"
else:
    grade="Fail"
print("Student name:",name)
print("Father name:",fname)
print("Roll number:",rno)
print(s1,"\t\t:",m1)
print(s2,"\t:",m2)
print(s3,"\t:",m3)
print(s4,"\t\t:",m4)
print(s5,"\t:",m5)
print("Total marks =500","\t\t","Obtained marks=",omarks)
print("Percentage","\t=",per,"%","\t","Grade","\t=",grade)
































from math import*
a=int(input("Enter first term:"))
d=int(input("Enter common difference:"))
n=int(input("Enter the nth term of the sequence:"))
tn=a+(n-1)*d
print("The nth term of the sequence is",tn)
x=input("Did you want to calculate the more terms?")
while(x=="yes"):
    n=int(input("Enter the nth term of the sequence:"))
    tn=a+(n-1)*d
    print("The nth term of the sequence is", tn)
    x=input("Did you want to calculate the more terms?")
else:
    print("finish")

