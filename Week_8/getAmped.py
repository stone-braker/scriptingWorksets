import shutil

shutil.copy('grid2.txt', 'g_rid.txt')


grid = list(open('g_rid.txt', 'r'))

# col = int(input('Enter Column:'))
# row = int(input('Enter Row:'))
# start = grid[col][row]
# lineList = [line.rstrip('\n') for line in open('g_rid.txt')]


def getFourCoord(fileVar, x, y):
    startSpace = specificChar(fileVar, x, y)

    if startSpace == '@':
        startSpace = '-'
        if x == 0:
            aboveC = fileVar[9][y]
        else:
            aboveC = fileVar[x - 1][y]
        if x == 9:
            belowC = fileVar[0][y]
        else:
            belowC = fileVar[x + 1][y]
        if y == 0:
            leftC = fileVar[x][9]
        else:
            lefC = fileVar[x][y - 1]
        if y == 9:
            rightC = fileVar[x][0]
        else:
            rightC = fileVar[x][y + 1]

        return 1 + getFourCoord(rightC) + getFourCoord(leftC) + getFourCoord(aboveC) + getFourCoord(belowC)
    else:
        return 0


# This needs to be a function to convert fileVar into a list of lists.
# lineOne = grid[0]
# linelist = lineOne.split()
# print(linelist)
# for x in range(len(linelist)):
#     print(linelist[x])


def linelist(fileVar, x):
    linE = fileVar[x]
    linElist = linE.split()
    return linElist


def specificChar(fileVar, x, y):
    line = linelist(fileVar, x)
    specificChar = line[y]
    return specificChar


testee = linelist(grid, 0)
print(testee)
testee2 = specificChar(grid, 0, 0)
print('\n', testee2)
if testee2 == '@':
    testee2 = '-'
print('\n', testee2)


#print(getFourCoord(grid, 0, 0))
