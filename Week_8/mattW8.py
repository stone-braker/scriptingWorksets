grid = list(open("grid.txt", "r"))
user_col = int(input('Enter column: '))
user_row = int(input('Enter row: '))
print("This is the symbol at the given coordinates: " +
      grid[user_col][user_row])
print("\nThis is how the grid prints out: ")


def printGrid(grid):
    for row in range(0, 10):
        for col in range(0, 10):
            print(grid[row][col], end=" ")
        print('\n')


printGrid(grid)

# print(grid)

#import sys
# sys.setrecursionlimit(900000000)
#
#file_e = open('grid.txt', 'r')
#file = file_e.readlines()
# file_e.close()
# file.reverse()
# for index, line in enumerate(file):
#    file[index] = line.split(' ')
#print(len(file)-1, len(file[0])-1)
#
#
# def end(file, y, x):
#
#    if y == len(file)-1 and x == len(file[0])-1:
#        return 1
#
#    try:
#        if file[y+1][x] == '0':
#            up = True
#    except:
#        pass
#    try:
#        if file[y][x+1] == '0':
#            right = True
#    except:
#        pass
#
#    try:
#        if up == True and right == True:
#            return end(file, y+1, x) + end(file, y, x+1)
#    except:
#        pass
#
#    try:
#        if up == True:
#            return end(file, y+1, x)
#    except:
#        pass
#
#    try:
#        if right == True:
#            return end(file, y, x+1)
#    except:
#        pass
#
#    if file[y+1][x] == '1' or file[y][x+1] == '1':
#        return 0
#
#
#print(end(file, 0, 0))
