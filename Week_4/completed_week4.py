def main():
    cardd = getInput()
    typee = getCardType(cardd)
    summ = sumOfDigits(cardd)
    vall = isValid(cardd)
    print(cardd, '\n', vall, '\n', typee)


def getInput():
    # HR1
    cardnumstr = input('Enter a credit card number:')
    return cardnumstr


def charToInt(digit):
    # HR2
    integerized = int(digit)
    return integerized


def doubledValue(number):
    # HR3
    doubled = number * 2
    if doubled < 10:
        return doubled
    elif doubled >= 10:
        doubled = str(doubled)
        return int(doubled[0]) + int(doubled[1])


def getCardType(cardNumber):
    # HR4
    if cardNumber[0] == "4":
        return "VISA"
    elif cardNumber[0] == "5":
        return "MASTERCARD"
    elif cardNumber[0] == "3" and cardNumber[1] == "4":
        return "AMERICAN EXPRESS"
    elif cardNumber[0] == "3" and cardNumber[1] == "7":
        return "AMERICAN EXPRESS"
    else:
        return "UNKNOWN ISSUER"


def sumOfDigits(cardNumber):
    # HR5
    rev_cardNumber = reverse_order(cardNumber)
    rev_odds = return_odds(rev_cardNumber)
    rev_evens = return_evens(rev_cardNumber)
    odd_list = []
    even_list = []
    for x in rev_odds:
        x = charToInt(x)
        odd_list.append(x)
    for y in rev_evens:
        y = charToInt(y)
        dub_y = doubledValue(y)
        even_list.append(dub_y)
    added_odds = sum(odd_list)
    added_evens = sum(even_list)
    altogethernow = added_odds + added_evens
    return altogethernow


def isValid(cardNumber):
    # HR6
    numer = sumOfDigits(cardNumber)
    print('\nTotal according to Luhn\'s method: ', numer)
    if numer % 10 == 0:
        return 'Valid number '
    else:
        return 'Not a valid number '


def reverse_order(cardNumstring):
    return cardNumstring[::-1]


def return_odds(s):
    return s[::2]


def return_evens(s):
    return s[1::2]


main()
