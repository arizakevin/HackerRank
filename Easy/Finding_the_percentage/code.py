if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    acum = 0
    for i in range(len(student_marks[query_name])):
        acum += student_marks[query_name][i]

    average = acum / len(student_marks[query_name])
    average = "{:.2f}".format(average)

    print(average)
