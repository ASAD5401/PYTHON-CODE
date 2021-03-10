import os
def duplicate(filename):
    with open(filename, "r") as f:
        words= set()
        for line in f.readlines():
            linewords=line.split()
            for word in linewords:
                if word in words:
                    return True
                words.add(word)
    return False
a=duplicate("d:\\ALI.txt")
print(a)