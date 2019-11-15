def reverse_string(s):
    return s[::-1]


def reverse_order(cardNum):
    cardNumstring = str(cardNum)
    length = len(cardNumstring)
    neg = -1
    rev_number = []
    for x in range(length):
        rev_dig = cardNumstring[neg]
        rev_number.append(rev_dig)
        neg -= 1
    return rev_number


def string_from_list(listy):
    empty_string = ""
    for x in listy:
        empty_string += x
    return empty_string


def doubledValue(number):
    # hiatt required, written by me
    doubled = number * 2
    if doubled < 10:
        return doubled
    elif doubled >= 10:
        doubled = str(doubled)
        return int(doubled[0]) + int(doubled[1])


def charToInt(digit):
    # hiatt required, written by me
    integerized = int(digit)
    return integerized


def sumOfDigits(cardNumber):
    # hiatt required, written by me
    rev_string = string_from_list(reverse_order(cardNumber))
    new_string = ""
    for x in rev_string:
        len_pos = rev_string.index(x)
        if len_pos == 0:
            len_pos = 1
            new_string += str(len_pos)
        if len_pos % 2 == 0:
            doubled = doubledValue(len_pos)
            new_string += str(doubled)
        else:
            new_string += str(len_pos)
    return new_string


cardNumb = 123456789123456789
goomba = string_from_list(reverse_order(cardNumb))
print(goomba)
