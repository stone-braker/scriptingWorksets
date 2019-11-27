import shutil

shutil.copy('grid2.txt', 'g_rid.txt')


grid = list(open('g_rid.txt', 'r'))

# col = int(input('Enter Column:'))
# row = int(input('Enter Row:'))
# start = grid[col][row]
# lineList = [line.rstrip('\n') for line in open('g_rid.txt')]

# the problem is i am still converting string to list in the recursion
# i need a copy that is lists of lists first
# so

# the problem now, is that the @ is not being changed in the fileVar, because it cannot be. becuase it is a string.
# so now i need to figure out how to do the same thing convertToLol() does but

#listGrid = convertToLoL(grid)


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


def linelist(fileVar, x):
    linE = fileVar[x]
    linElist = linE.split()
    return linElist


def specificChar(fileVar, x, y):
    line = linelist(fileVar, x)
    specificChar = line[y]
    return specificChar


def convertToLoL(gridVar):
    emptyList = []
    for x in range(len(grid)):
        line = gridVar[x]
        linelist = line.split()
        emptyList.append(linelist)
    return emptyList


listGrid = convertToLoL(grid)
#print('1', listGrid)
#print('2', listGrid[0][0])
#testVar = listGrid[0][0]
#print('3', testVar)
#testVar = '-'
#print('4', testVar)
#print('5', listGrid[0][0])
#listGrid = '-'
#print('6', listGrid[0][0])

print(getFourCoord(listGrid, 0, 0))

#            aboveC = fileVar[9][y]
#        else:
#            aboveC = fileVar[x - 1][y]
#        if x == 9:
#            belowC = fileVar[0][y]
#        else:
#            belowC = fileVar[x + 1][y]
#        if y == 0:
#            leftC = fileVar[x][9]
#        else:
#            lefC = fileVar[x][y - 1]
#        if y == 9:
#            rightC = fileVar[x][0]
#        else:
#            rightC = fileVar[x][y + 1]
#        return 1 + getFourCoord(rightC) + getFourCoord(leftC) + getFourCoord(aboveC) + getFourCoord(belowC)

# This needs to be a function to convert fileVar into a list of lists.
# lineOne = grid[0]
# linelist = lineOne.split()
# print(linelist)
# for x in range(len(linelist)):
#     print(linelist[x])


#testee = linelist(grid, 0)
# print(testee)
#testee2 = specificChar(grid, 0, 0)
#print('\n', testee2)
# if testee2 == '@':
#    testee2 = '-'
#print('\n', testee2)
