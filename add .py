#a=[[1,2,3],[4,5,6],[7,8,9]]
#b=[[1,2,3],[4,5,6],[7,8,9]]
#c=[[0,0,0],[0,0,0],[0,0,0]]
#for i in range(len(a)):
#    for j in range(len(a[0])):
 #       c[i][j]=a[i][j]+b[i][j]
  #      print(c[i][j],end="\t")
   # print(" ")
n=4
a=[64,30,25,33]
a.sort()
threshold=2
d=2
c=0
q=a[::-1]
v=q
cou=0
p=list()
while(c!=threshold):
    for k in range(n):
        q[k]=q[k]//d
        cou+=1
        for i in range(n):
            for j in range(n):
                if(q[i]==q[j]):
                    c+=1
                    if(c==threshold):
                        m=q[0]
                        w=q
                        for xz in range(threshold):
                            w.remove(m)
                        for x in range(n-threshold,0,-1):
                            p.append(v[x])
                        print(p)
                        print(w)
                        print(q)
                        print(v[p[0]])
                        print(cou)
                        break
            if(c==threshold):
                break
            c=0
        if (c == threshold):
            break