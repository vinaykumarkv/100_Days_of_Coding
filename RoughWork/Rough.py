n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input("name and score separated by space ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input("whose avg score do you need? : ")


def avg_score(names):
    score = student_marks[names]
    a = 0
    for i in range(len(score)):
        a += score[i]
        return a / len(score)


print(avg_score(query_name))
