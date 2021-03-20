#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math
import sys


def function():  # a large function i won't put here
    a = int(input('Input variable "a": '))
    if a > 0:
        x = round(-math.fabs(a - 1) / (2 * a), 4)
    else:
        x = round(math.log10(math.sqrt(1 + math.pow(a, 2))), 4)
    print(f'Function root = {x}')


def comparison():  # compares several functions
    x = int(input('Input variable "x": '))
    ch = round(math.cosh(x), 2)
    mod = round(1 + math.fabs(x), 2)
    power = round(math.pow((1 + x), x), 2)
    print('')

    if ch > mod:
        if mod > power:
            print(power, mod, ch)
        else:
            print(mod, power, ch)
    else:
        if mod > ch:
            if ch > power:
                print(power, ch, mod)
            else:
                print(ch, power, mod)


def runner():  # easier function navigation
    print('Type for available functions: ')
    print('1 for Function')
    print('2 for Functions comparison')
    run = input('...or "exit" to leave the program: ')
    print('')

    if run == '1':
        return function()
    elif run == '2':
        return comparison()
    elif run == 'exit' or run == 'Exit':
        sys.exit()
    else:
        print('Wrong input, try again')


while True:
    runner()
    print('')
