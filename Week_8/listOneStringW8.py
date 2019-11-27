import shutil

shutil.copy('grid2.txt', 'g_rid.txt')


grid = list(open('g_rid.txt', 'r'))

# col = int(input('Enter Column:'))
# row = int(input('Enter Row:'))
# start = grid[col][row]
# lineList = [line.rstrip('\n') for line in open('g_rid.txt')]

# I have to change the string at grid[0] to a list in order to change the elements inside of it


def getFourCoord(fileVar, x, y):

    amperCount = 0
    startSpace = fileVar[x][y]

    if startSpace == '@':
        amperCount += 1
        returnCount = amperCount
        fileVar[x][y] = '-'
        return amperCount + getFourCoord(fileVar, x, y - 1) + getFourCoord(
            fileVar, x, y + 1) + getFourCoord(fileVar, x - 1, y) + getFourCoord(fileVar, x + 1, y)
    else:
        return 0


lineOne = grid[0]
linelist = lineOne.split()
print(linelist)
for x in range(len(linelist)):
    print(linelist[x])
