def getListData():
    scores = []
    n = int(input("Enter number of grades : "))
    for num in range(0, n):
        grd = int(input('Enter Grade #', num))
        scores.append(grd)
    return scores
