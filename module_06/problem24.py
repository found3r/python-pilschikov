#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math


def ternary_digit(digit):  # Turns the number into ternary system

    # If the input number is '1'  this function simply ignores it, because of line 22.
    # Any changes to the cycle make all the calculations false, so I created
    # this check as the final 'for'-cycle will require to print '1' anyways.

    if digit == 1:
        print(1)
    else:
        power = 0
        ternary_list = []  # Creates digits sequence which is the actual number in ternary
        counter = 0  # Counts times power is in the number
        ternaried = math.pow(3, power)

        while digit > ternaried:  # Finds the highest power value
            power = power + 1
            ternaried = math.pow(3, power)
            if ternaried == digit:
                power = power + 1

        for x in reversed(range(power)):  # Finds amount of times power is in number
            while digit > 0:
                digit = digit - math.pow(3, x)
                counter = counter + 1
            if digit < 0:
                digit = digit + math.pow(3, x)
                counter = counter - 1
            ternary_list.append(counter)
            counter = 0

        print(*ternary_list, sep='')


n = int(input('Input a number (n > 0): '))
while n <= 0:
    print('Wrong input')
    n = int(input('Input a number (n > 0): '))
for runner in range(0, n + 1):
    ternary_digit(runner)
