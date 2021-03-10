def average(array):
    # your code goes here
    a=set(array)
    b=list(a)

    w=sum(b)
    y=len(b)
    t=w/y
    x="{0:.3f}".format(t)
    return x

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)