#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import string


def one_to_nine():  # This function creates a 9x9 table with an increasing digit per row
    digit = 1  # The first number used in the table
    row_positions = 9  # Total amount of positions per row
    row_list = []
    for row in range(row_positions):  # Creates rows
        for columns in range(row_positions):  # Prints digits in rows
            row_list.append(0)  # Fills the row with zeros
        position_in_row = digit - 1  # As listing starts with zero
        row_list[position_in_row] = digit  # Puts digit on digit-numbered position in row
        print(*row_list)
        digit = digit + 1  # Next digit
        row_list.clear()


def descend():  # This function creates a 9x9 table with decreasing
    # numbers and their amount per row
    digit = 9  # The first number in the table
    row_positions = 9
    row_list = []
    zero_space = 0  # The amount of zeros to put before numbers
    for row in range(row_positions):
        for columns in range(row_positions):
            row_list.append(digit)
        for position in range(zero_space):  # Numbers to zeros before main position
            row_list[position] = 0
        zero_space = zero_space + 1
        digit = digit - 1
        print(*row_list)
        row_list.clear()


def scroll():  # This function creates a 10x10 table with scrolling digits 0-9
    digits_list = []
    for number in string.digits:  # Creates a list of the digits
        digits_list.append(number)
    print(*digits_list)  # Easier first row output
    rows_amount = 8  # As the first one is used
    for row in range(rows_amount):  # Prints next scrolled row
        digits_list = digits_list[-1:] + digits_list[:-1]
        print(*digits_list)

one_to_nine()
print('')
descend()
print('')
scroll()
