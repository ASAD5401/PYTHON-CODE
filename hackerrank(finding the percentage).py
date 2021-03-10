
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
a=student_marks[query_name]
s=sum(a)/3
q=round(s,2)
print("{0:.2f}".format(q))
