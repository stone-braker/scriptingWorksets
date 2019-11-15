def reverse_string(s):
    return s[::-1]


def string_from_list(listy):
    # use this instead... variable = "".join str(x for x in listy) method
    # my way only works if list consists of strings - concatenation doesn't work with integers
    empty_string = ""
    for x in listy:
        empty_string += x
    return empty_string


def reverse_order(cardNumstring):
    return cardNumstring[::-1]

# this one sucks cuz its a list at the end
# def reverse_order_as_list(cardNum):
#    cardNumstring = str(cardNum)
#    length = len(cardNumstring)
#    neg = -1
#    rev_number = []
#    for x in range(length):
#        rev_dig = cardNumstring[neg]
#        rev_number.append(rev_dig)
#        neg -= 1
#    return str(rev_number)


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
    rev_list = reverse_order(cardNumber)
    new_list = []
    for x in rev_list:
        indeX = rev_list.index(x)
        print(indeX)
        if index == 0:
            int_x = int(x)
            new_list.append(int_x)
        if index == 1:
            char_x = charToInt(x)
            dub_x = doubledValue(char_x)
            new_list.append(dub_x)
        if index % 2 == 0:
            int_x = int(x)
            new_list.append(int_x)
        else:
            char_x = charToInt(x)
            dub_x = doubledValue(char_x)
            new_list.append(dub_x)

    print(new_list)
    print('The sum equals', sum(new_list))
    if sum(new_list) % 10 == 0:
        print('Valid card')
    else:
        print('Invalid:')


# sumOfDigits(79927398713)
listy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listyABC = ['a', 'b', 'c', 'd', 'e', 'f']
# print(reverse_order(123456789))
# joins list of integers as combined string without white spaces
joined_listy = "".join(str(x) for x in listy)
print("my function", string_from_list(listyABC))
print(joined_listy)
revList = reverse_order(joined_listy)
print(revList)


# first number: 79927398713  = 70
