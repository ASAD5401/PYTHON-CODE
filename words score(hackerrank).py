

def score_words(a):
    c=0
    f=0
    for i in a:
        for j in i:
            if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="y"):
                c+=1
        if(c%2==0):
            f+=2
        else:
            f+=1
        c=0
    return f




n = int(input())
words = input().split()
print(score_words(words))