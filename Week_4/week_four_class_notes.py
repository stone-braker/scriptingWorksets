def sumOfDigits(cardNumber):
    rev_list = reverse_order(cardNumber)
    new_str = ""
    for x in rev_list:
        indeX = rev_list.index(x)
        print(indeX)
        if indeX % 1 == 0:
            int_x = int(x)
            new_string +=
            # then add it to string not list
            # new_list.append(int_x)
        if indeX == 1:
            char_x = charToInt(x)
            dub_x = doubledValue(char_x)
            new_list.append(dub_x)
        if indeX % 2 == 0:
            int_x = int(x)
            new_list.append(int_x)
        else:
            char_x = charToInt(x)
            dub_x = doubledValue(char_x)
            new_list.append(dub_x)


# Ok, the mod % 1 == 0 is EVERYTHING,
# then you only need to exclude the others with even numbers
# need if index % 2 == 0: to be first, then the index
# so, if index == 0, don't double, just add to new string
# if index % 2 == 0, don't, double, jsut add to new string
# else: double and add to string
