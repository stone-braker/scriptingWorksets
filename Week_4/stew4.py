import time

# main function controls logic flow of program and end output to user


def main():
    crdnum = get_input()
    print(crdnum)  # test print
    crdtype = card_type(crdnum)
    print(crdtype)  # test print
    valid_num = is_valid(crdnum)
    print(valid_num)

# intake information from user and check that input is all numeric characters


def get_input():
    cnum = input("Enter card number...")
    if cnum.isnumeric():
        return cnum
    else:
        print("Please enter only numeric characters.")
        time.sleep(3)
        main()

# check to see what type of card the string of numeric characters could represent


def card_type(c):
    x = slice(1)
    y = slice(2)
    if c[x] == "4":
        return "Visa"
    elif c[x] == "5":
        return "MasterCard"
    elif c[y] == "34" or c[y] == "37":
        return "American Express"
    else:
        return "Unknown"

# function to check if final generated number is valid


def is_valid(c):
    number = sum_of_digits(c)
    if number % 10 == 0:
        x = "Valid number"
        return x
    else:
        x = "Not a valid number"
        return x

# function generates sum of numbers to be validated


def sum_of_digits(str):
    num_sum = 0
    num_list = char_to_int(str)
    # print(num_list) # test print of reversed list
    for num in range(1, len(num_list), 2):
        x = double_digit(num)
        num_sum += x
    for num in range(0, len(num_list), 2):
        num_sum += num
    return num_sum

# convert string of numeric characters to reversed list of integers


def char_to_int(str):
    int_list = []
    for x in str:
        int_list.append(int(x))
    int_list.reverse()
    return int_list

# doubles integer, if result is 2 digits ... adds digits together and returns sum,
# otherwise returns single digit doubled integer


def double_digit(num):
    num_sum = 0
    num = num * 2
    if len(str(num)) > 1:
        for x in range(0, len(str(num))):
            num_sum += int(x)
        return num_sum
    else:
        return num


# call main function
if __name__ == "__main__":
    main()
