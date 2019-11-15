from math import sqrt


def main():
    classScores = getListDataAsString()
    print("Class Scores:", classScores)
    classAvg = average(classScores)
    print("The average is: ", classAvg)
    classSD = standardDeviation(classScores)
    print("The standard deviation is: ", classSD)
    counter = 1
    for x in classScores:
        print("Student:", counter, "Score:", x, "%", "Curved Grade:",
              getLetterGrade(x, classAvg, float(classSD)))
        counter += 1


def getListDataAsString():
    classScores = input("Enter 10 scores:")
    scoreList = classScores.split()
    intList = []
    for x in scoreList:
        x = int(x)
        intList.append(x)
    return intList


def recursiveInput():
    students = int(input('Enter Number of Grades:'))
    gradeList = []

    def recGradeList(students):
        if students > 0:
            nextGrade = int(input('Enter Grade:'))
            gradeList.append(nextGrade)
            recGradeList(students - 1)
    return gradeList


def getListData():
    scores = []
    n = int(input("Enter number of grades : "))
    for num in range(0, n):
        grd = int(input('Enter Grade {}:'.format(num + 1)))
        scores.append(grd)
    return scores


def average(scores):
    meany = sum(scores) / len(scores)
    return meany


def standardDeviation(scores):
    mean = average(scores)
    sqList = []
    for x in scores:
        sqDiff = (x - mean) ** 2
        sqList.append(sqDiff)
    sqAvg = average(sqList)
    stanDev = sqrt(sqAvg)
    return '{:.1f}'.format(stanDev)


def getLetterGrade(score, mean, stdDev):
    if score > mean:
        diffPos = score - mean
        if diffPos > stdDev:
            grade = 'A'
        elif diffPos > stdDev / 2:
            grade = 'B'
        else:
            grade = 'C'
    if score < mean:
        diffNeg = mean - score
        if diffNeg > stdDev:
            grade = 'F'
        elif diffNeg > stdDev / 2:
            grade = 'D'
        else:
            grade = 'C'
    return grade


main()
#testArray = [70, 85, 75, 65, 82, 96, 58, 93, 86, 90]
# getListDataAsString()
