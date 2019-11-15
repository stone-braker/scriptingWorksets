rev_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in rev_list:
    index = rev_list.index(x)
    print(index)

sturing = "i love strings, and cheeesese"


def reverse_string(s):
    return s[::-1]


def sumOfDigits(cardNumber):
    # this is the way i initially intended to do the function
    # i can still go this way if idea falls through,
    # just use strings, not lists i think it'll be easier to
    # go back and forth between user input and such
    rev_cardNumber = reverse_order(cardNumber)
    proc_cardNumber = ""
    for x in rev_cardNumber:
        indy = rev_cardNumber.index(x)
        print(indy)


print(reverse_string(sturing))

list_to_string = ['The', 'Python', 'Tut']
str_join = "".join(list_to_string)
print(str_join)
