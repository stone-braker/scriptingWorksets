# functions Hiatt said we MUST have in our program:
def reverse_string(s):
    return s[::-1]


def reverse_order(cardNumstring):
    # broken first try
    length = len(cardNumstring)
    neg = -1
    rev_number = []
    for x in range(length):
        rev_dig = cardNumstring[neg]
        rev_number.append(rev_dig)
        neg -= 1
    return rev_number


def string_from_list(listy):
    # again, me
    empty_string = ""
    for x in listy:
        empty_string += x
    return empty_string


def getInput(prompt):
    # hiatt required, written by me
    # Takes in a string as a parameter - prints that to the console
    # then gets a string of input from the console and returns the input.
    str_prompt = str(prompt)
    print(str_prompt)
    string_input = input("Enter a card number: ")
    return string_input


def charToInt(digit):
    # hiatt required, written by me
    integerized = int(digit)
    return integerized


def doubledValue(number):
    # hiatt required, written by me
    doubled = number * 2
    if doubled < 10:
        return doubled
    elif doubled >= 10:
        doubled = str(doubled)
        return int(doubled[0]) + int(doubled[1])


def sumOfDigits(cardNumber):
    # hiatt required, written by me
    rev_string = string_from_list(reverse_order(cardNumber))
    new_string = ""
    for x in rev_string:
        x = chartoInt(x)
        if rev_string[x] % 2 == 0:
            y = doubledValue(rev_string[x])
            new_string += y
        else:
            new_string += x
    return new_string

    # Sums the digits of a credit card number according to the Luhn algorithm.
    # i.e. calling sumOfDigits("79927398713") should result in 70.
    # This should make use of charToInt and doubledDigitValue.


# def isValid(cardNumber):
    # Returns true / false indicating if a credit card number is potentially a valid number according to Luhn algorithm.
    # (This should use a call to sumOfDigits!)


# def getCardType(cardNumber):
    # Returns a string representing the type of credit card a number is:
    # Visa, MasterCard, American Express, or Unknown

print(doubledValue(4))
print(doubledValue(8))

test = "1234455656"
print(reverse_order(test))
############
#
#    Hint: the algorithm is supposed to work from right to left.
#    Start by just printing out the string one char at a time in reverse order.
#    Then worry about actually adding up their values. Don't forget that every second one gets doubled.
#
#    isValid(cardNumber);
#    Returns true/false indicating if a credit card number is potentially a valid number according to Luhn algorithm. (This should use a call to sumOfDigits!)
#
#    getCardType(cardNumber);
#    Returns a string representing the type of credit card a number is: Visa, MasterCard, American Express, or Unknown.
