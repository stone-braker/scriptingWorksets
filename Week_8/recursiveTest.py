gradeList = []


def recGradeList(x):
    if x > 0:
        nextGrade = int(input('Enter Grade:'))
        gradeList.append(nextGrade)
        recGradeList(x - 1)
    return gradeList


def recursiveInput():
    students = int(input('Enter Number of Grades:'))
    grades = recGradeList(students)
    print(grades)
    return grades


recursiveInput()
