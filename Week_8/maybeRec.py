grid = list(open('grid2.txt', 'r'))


def main():
    col = int(input('Enter Column:'))
    row = int(input('Enter Row:'))
    print(getFourCoord(listGrid, col, row), 'cells')


def getFourCoord(fileVar, x, y):
    if fileVar[x][y] == '@':
        fileVar[x][y] = '-'
        if x == 0 and y == 0:
            return 1 + getFourCoord(fileVar, x, 9) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, 9, y) + getFourCoord(fileVar, x + 1, y)
        elif x == 0 and y == 9:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, 0) + getFourCoord(fileVar, 9, y) + getFourCoord(fileVar, x + 1, y)
        elif x == 9 and y == 0:
            return 1 + getFourCoord(fileVar, x, 9) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, 0, y)
        elif x == 9 and y == 9:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, 0) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, 0, y)
        elif x == 0 and y != 0 and y != 9:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, 9, y) + getFourCoord(fileVar, x + 1, y)
        elif x == 9 and y != 0 and y != 9:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, 0, y)
        elif y == 0 and x != 0 and x != 9:
            return 1 + getFourCoord(fileVar, x, 9) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, x + 1, y)
        elif y == 9 and x != 0 and x != 9:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, 0) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, x + 1, y)
        else:
            return 1 + getFourCoord(fileVar, x, y - 1) + getFourCoord(fileVar, x, y + 1) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, x + 1, y)
    else:
        return 0


def convertToLoL(gridVar):
    emptyList = []
    for x in range(len(grid)):
        line = gridVar[x]
        linelist = line.split()
        emptyList.append(linelist)
    return emptyList


listGrid = convertToLoL(grid)
main()
