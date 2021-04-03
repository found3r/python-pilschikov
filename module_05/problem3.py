#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import sys
import math


def divisor():  # Greatest divisor of two numbers
    greatest_divisor = 1
    first_number = int(input('Input the first positive number: '))
    while first_number <= 0:
        print('Wrong input')
        first_number = int(input('Input the first positive number: '))
    second_number = int(input('Input the second positive number: '))
    while second_number <= 0:
        print('Wrong input')
        second_number = int(input('Input the second positive number: '))
        print(' ')

    if first_number % second_number == 0:
        print(f'{second_number} is the greatest divisor')
    elif second_number % first_number == 0:
        print(f'{first_number} is the greatest divisor')
    else:
        term_divisor = 2
        while (term_divisor < first_number) and (term_divisor < second_number):
            while (first_number % term_divisor == 0) and (second_number % term_divisor == 0):
                first_number = first_number // term_divisor
                second_number = second_number // term_divisor
                greatest_divisor = greatest_divisor * term_divisor
            term_divisor = term_divisor + 1
        print(f'{greatest_divisor} is the greatest divisor')


def neg_finder():  # Finds the first negative number of cos(ctg(n))
    n = 1
    while math.cos(1 / math.tan(n)) >= 0:
        n = n + 1
    print(n)


def runner():  # easier function navigation
    print('Type for available functions: ')
    print('1 for Greatest divisor')
    print('2 for Negative finder')
    run = input('...or "exit" to leave the program: ')
    print('')

    if run == '1':
        return divisor()
    elif run == '2':
        return neg_finder()
    elif run == 'exit' or run == 'Exit':
        sys.exit()
    else:
        print('Wrong input, try again')


while True:
    runner()
    print('')
