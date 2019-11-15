# You must use functions to simplify main.
# For full credit you should have functions that take
# care of these tasks. You can add more if you like.
from math import sqrt

# average is 80.0
# standard deviation is 11.9
# Grades: D, C, C, F, C, A, F, A, B, B]


def main():
    classScores = getListData()
    print("Class Scores:", classScores)
    classAvg = average(classScores)
    print("The average is: ", classAvg)
    classSD = standardDeviation(classScores)
    print("The standard deviation is: ", classSD)
    counter = 1
    for x in classScores:
        print("Student:", counter, "Grade:",
              getLetterGrade(x, classAvg, float(classSD)))
        counter += 1


def getListData():
    scores = []
    n = int(input("Enter number of grades : "))
    for i in range(0, n):
        grd = int(input('Enter Next Grade:'))
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


#testArray = [70, 85, 75, 65, 82, 96, 58, 93, 86, 90]
#testlist = (1, 2, 1, 2, 1, 2, 1, 2)
# print(average(testArray))
# print(standardDeviation(testArray))
#myGrade = getLetterGrade(90, 80, 11.9)
# print(myGrade)
# print(classOneScores)
main()
