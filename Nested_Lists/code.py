def getSecondLowestGrade(student):
    if student[1] == secondLowest:
        return student

if __name__ == '__main__':
    students = []
    lowest = None
    secondLowest = None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if lowest is None or lowest < score:
            lowest = score
        if secondLowest is None or (secondLowest < score and score > lowest):
            secondLowest = score

    secondLowestsStudents = filter(getSecondLowestGrade, students)
    secondLowestsStudents = sorted(
        secondLowestsStudents,
        key=lambda student:
        student[0]
    )

    for i in range(len(secondLowestsStudents)):
        print(secondLowestsStudents[i][0])
