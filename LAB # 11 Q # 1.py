l1=[5,9,3,8,12]
l2=[2,0,1,5]
for i in range(len(l1)):
    try:
        a=l1[i]%l2[i]
        print("When",l1[i],"is divided by",l2[i],"remainder is",a)
    except IndexError:
        print("out of range")
    except ZeroDivisionError:
        print(" math error")
