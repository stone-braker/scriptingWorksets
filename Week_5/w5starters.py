import random


# Option 1
def printKey(puzzle):
    for row in range(0, 10):
        for col in range(0, 10):
            print(puzzle[row][col], end=" ")
        print('\n')

# Option 2


def printPuzzle(puzzle):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for row in range(0, 10):
        for col in range(0, 10):
            if puzzle[row][col] == '_':
                print(random.choice(LETTERS), end=" ")
            else:
                print(puzzle[row][col], end=" ")

        print('\n')

# Option 3


def addHorzWord(puzzle):
    row = int(input("enter row: "))
    col = int(input("enter column: "))
    word = input("enter word: ")

    for i in range(0, len(word)):
        puzzle[(row-1)][(col-1)+i] = word[i].upper()

# Option 4


def addVertWord(puzzle):
    row = int(input("enter row: "))
    col = int(input("enter column: "))
    word = input("enter word: ")

    for i in range(0, len(word)):
        puzzle[(row-1)+i][(col-1)] = word[i].upper()

# Option 5


def checkHorizFit(puzzle):
    row = int(input("enter row: "))
    col = int(input("enter column: "))
    word = input("enter word: ")
    fits = True

    if (((col-1)+len(word)) > 9):
        fits = False
    else:
        for x in range(0, len(word)):
            if puzzle[(row-1)][(col-1)+x] != '_':
                if puzzle[(row-1)][(col-1)+x] != word[x].upper():
                    fits = False

    if fits:
        print("Fits")
    else:
        print("Doesn't fit")

# Option 6


def checkSpaceCount(puzzle):
    counter = 0
    for words in puzzle:
        counter += words.count('_')
    print(counter)


def main():

    # This makes it a 10x10
    puzzle = [
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    ]

    # Menu
    menu = {}
    menu['1'] = "Print key"
    menu['2'] = "Print puzzle"
    menu['3'] = "Add horizontal word"
    menu['4'] = "Add vertical word"
    menu['5'] = "Check horizontal fit"
    menu['6'] = "Space count"
    menu['8'] = "Quit"
    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select:")
        if selection == '1':
            printKey(puzzle)
        elif selection == '2':
            printPuzzle(puzzle)
        elif selection == '3':
            addHorzWord(puzzle)
        elif selection == '4':
            addVertWord(puzzle)
        elif selection == '5':
            checkHorizFit(puzzle)
        elif selection == '6':
            checkSpaceCount(puzzle)
        elif selection == '8':
            return
        else:
            print("Unknown Option Selected!")


main()
