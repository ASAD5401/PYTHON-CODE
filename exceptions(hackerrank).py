n=int(input())
for i in range(n):
    a=str(input()).split()

    try:
        s = int(a[0])
        d = int(a[1])
        r=s/d
        print(int(r))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)