n=int(input())
for i in range(n):
    a=str(input())
    if(len(a)==10):
        if(a.isnumeric()):

            if(a[0]=="7" or a[0]=="8" or a[0]=="9"):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")