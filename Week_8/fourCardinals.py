# Define functions for the Four Cardinals:
def lkLeft(grid, x=col, y=row):
    leftSymbol = fileVar[x][y - 1]
    if leftSymbol == '@':
        leftSymbol = '-'
        return 1
    else:
        return 0


def lkRight(grid, x=col, y=row):
    rightSymbol = fileVar[x][y + 1]
    if rightSymbol == '@':
        surroundAmpers = getFourCoord(rightSymbol)
        rightSymbol = '-'
        return 1
    else:
        return 0


def lkAbove(grid, x=col, y=row):
    aboveSymbol = fileVar[x - 1][y]
    if aboveSymbol == '@':
        aboveSymbol = '-'
    return 1
    else:
        return 0


def lkBelow(fileVar=grid, x=col, y=row):
    belowSymbol = fileVar[x + 1][y]
    if belowSymbol == '@':
        belowSymbol = '-'
        return 1
    else:
        return 0

# First FourCoord function:


def getFourCoord(startSpace=grid[col][row]):
    amperCount = 0
    if startSpace == '@':
        amperCount += 1
        startSpace = '-'
        surroundAmps = getFourCoord(lkLeft(startSpace)) + getFourCoord(lkRight(
            startSpace)) + getFourCoord(lkAbove(startSpace)) + getFourCoord(lkBelow(startSpace))
        return amperCount + surroundAmps
    else:
        return 0
