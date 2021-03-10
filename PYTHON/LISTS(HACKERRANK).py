l=list()
for i in range(int(input())):
    x=str(input()).split(" ")
    command=x[0]
    if command=="insert":
        l.insert(int(x[1]),int(x[2]))
    elif command=="print":
        print(l)
    elif command=="remove":
        l.remove(int(x[1]))
    elif  command=="sort":
        l.sort()
    elif command=="append":
        l.append(int(x[1]))
    elif command=="pop":
        l.pop()
    elif command=="reverse":
        l.reverse()
