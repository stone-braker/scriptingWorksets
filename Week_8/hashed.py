import shutil

shutil.copy('grid.txt', 'g_rid.txt')


grid = list(open("g_rid.txt", "r"))


# def hashie_search():
#   -for user_entered_index:
#       if (location above, below, and side to side have hashies, == @:
'''so there needs to be a recursive function to 
    call on each space, and if there are more than one
    hashies surrounding selected space, then what? do it for 
    both? how?'''
# then, do hashie_search on those spaces
#
# how to find each space around it relevant to entered starting index.
# that's the main function

if user enters in [1, 1] come into grid, look at[1, 1] if ampersand,
need to do recursive getAmper(): function four times to check all surrounding spaces.
for spaces on edges, notes already taken.


for direction in (list of directional equivalents)

build grid in memory, take copy of it, and then for space in surroundingSpaces
if ampersand change to '-' after copying to counter.
goes through and clears spaces and avoids backtrack.
once you get to spot where everything around is a '-', you're done, return counter for ampersands.


When Calculating WrapAround:

if n-1 = -1:
    then n equals 9
if n+1 = 10:
    then n equals 0

How to Calculate Number of Spaces With More Than One Surrounding Ampersand:

no idea.


look at in-depth memory functionality of Python as per Hiatt

Recursive Function Call:

when these spiders go out top right bottom left, they don't keep counting themselves, change each '@' to '-'


def isAmper(input):
    if input == '@':
        count = 1
    if input == '-':
        count = 0
    return count


def recursiveCheck(x, y):
    if symbol at postition[x, y] == '-'
    return 0
    blank = isAmper(position[x, y])
    if blank == 1:
        return 1
        blank == '-'

    else:
        above = isAmper(position[x-1, y])
        below = isAmper(position[x+1, y])
        left = isAmper(position[x, y-1])
        right = isAmper(position[x, y+1])
        return above + below, left, right


# List of fourCardinals:

[Left= y - 1, unless 0 then 9]
[Right= y + 1, unless 9 then 0]
[Up= x - 1, unless 0 then 9]
[Down= x + 1, unless 9 then 0]
