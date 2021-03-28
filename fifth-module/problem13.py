#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math
import sys


def n_function():  # Factorial of (2*n - 1) function
    number = int(input('Input a positive number: '))
    if number <= 0:
        while number <= 0:
            print('Wrong input')
            number = int(input('Input a positive number: '))
    result = math.factorial(2 * number - 1)
    print(f'Function result is {result}')


def double_double_factorial():  # Double factorial of 2n function
    number = int(input('Input a positive number: '))
    if number <= 0:
        while number <= 0:
            print('Wrong input')
            number = int(input('Input a positive number: '))
    result = math.factorial(math.factorial(2 * number))
    print(f'Function result is {result}')


def double_factorial():  # Double factorial
    number = int(input('Input a positive number: '))
    if number <= 0:
        while number <= 0:
            print('Wrong input')
            number = int(input('Input a positive number: '))
    result = math.factorial(math.factorial(number))
    print(f'Function result is {result}')


def runner():
    print('Type for available functions: ')
    print('1 for Factorial of 2n - 1')
    print('2 for Double factorial of 2n')
    print('3 for Double factorial')
    run = input('...or "exit" to leave the program: ')
    print('')

    if run == '1':
        return n_function()
    elif run == '2':
        return double_double_factorial()
    elif run == '3':
        return double_factorial()
    elif run == 'exit' or run == 'Exit':
        sys.exit()
    else:
        print('Wrong input, try again')


while True:
    runner()
    print('')