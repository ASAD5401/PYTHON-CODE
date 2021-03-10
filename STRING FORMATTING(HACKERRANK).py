def print_formatted(n):
    # your code goes here
    w = len(str(bin(n))[2:])
    for i in range(1, n + 1):
        z = oct(i)
        x = hex(i)
        c = bin(i)
        print((str(i)).rjust(w), (str(z[2:])).rjust(w), (str(x[2:].upper())).rjust(w), (str(c[2:])).rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)