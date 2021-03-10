# Python3 code to implement Jump Search


import math
a=15
print(math.sqrt(a))
def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
    if arr[int(prev)] == x:
        return prev
    return -1
arr=[ 0, 1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89, 144, 233,377,610,700]
#     0  1  2  3  4  5  6   7   8  9   10  11  12   13  14  15  16
x =610
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number", x, "is at index", "%.0f" % index)

# This code is contributed by "Sharad_Bhardwaj".
