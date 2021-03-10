l=list()
import os
def distribution(filename):
       filename=open(filename)
       s=filename.read().split()
       print("The student who got A+ are :",(s.count("A+")))
       print("The student who got A  are :",(s.count("A")))
       print("The student who got B  are :",(s.count("B")))
       print("The student who got C  are :",(s.count("C")))
       print("The student who got D  are :",(s.count("D")))
filename=input("Enter filename that you want to open:")
distribution(filename)