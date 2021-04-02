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


def graph():  # graph crossing
    print('System of equations appears in such form:')
    print('a1*x + b1*y = c1')
    print('a2*x + b2*y = c2')
    a1 = int(input('Input variable "a1": '))
    b1 = int(input('Input variable "b1": '))
    c1 = int(input('Input variable "c1": '))
    a2 = int(input('Input variable "a2": '))
    b2 = int(input('Input variable "b2": '))
    c2 = int(input('Input variable "c2": '))

    if (a1 == a2) and (b1 == b2) and (c1 != c2):
        print('Graphs do not cross')
    elif (a1 == a2) and (b1 == b2) and (c1 == c2):
        print('Graphs have infinite amount of cross points')
    else:
        n = a1 / a2
        y = (n * c2 - c1) / (n * b2 - b1)
        x = (c1 - b1 * y) / a1
        print(f'x = {x}')
        print(f'y = {y}')


def function_power():  # ax^4 + bx^2 + c = 0 equation solvation
    print('Equation appears in such form:')
    print('a*x^4 + b*x^2 + c = 0 (a != 0)')
    a = int(input('Input variable "a": '))
    while a == 0:
        print('Incorrect value of "a"')
        a = int(input('Input variable "a": '))
    b = int(input('Input variable "b": '))
    c = int(input('Input variable "c": '))
    print('')

    y1 = (-b + (b ** 2 - 4 * a * c)) / 2 * a
    y2 = (-b - (b ** 2 - 4 * a * c)) / 2 * a

    if y1 < 0:
        print(f'x = {round(math.pow(y2, 1 / 2), 2)}')
    elif y2 < 0:
        print(f'x = {round(math.pow(y1, 1 / 2), 2)}')
    else:
        print(f'x1 = {round(math.pow(y1, 1 / 2), 2)}')
        print(f'x2 = {round(math.pow(y2, 1 / 2), 2)}')


def triangle():  # Triangle check
    print('Input triangle side lengths')
    a = int(input('Input variable "a": '))
    b = int(input('Input variable "b": '))
    c = int(input('Input variable "c": '))
    print('')

    if a == b == c:
        print('3')
    elif (a == b) or (b == c) or (c == a):
        print('2')
    elif (a + b < c) or (a + c < b) or (c + b < a):
        print('0')
    else:
        print('1')


def position():  # Position check in 10-99 sequence
    k = int(input('Input position: '))
    print('')
    n = 10
    sequence = ''
    while n < 100:
        sequence = sequence + str(n)
        n = n + 1
    sequencelist = list(sequence)
    print(f'Digit on position {k} = {sequencelist[k]}')


def infinity(): # 10 order position check
    oneposition = 1
    n = 1
    k = int(input('Input position: '))
    print('')

    while n < k:
        n = n + oneposition
        oneposition = oneposition + 1

    if n == k:
        print(f'Digit on postion {k} = 1')
    else:
        print(f'Digit on postion {k} = 0')


def runner():  # easier function navigation
    print('Type for available functions: ')
    print('1 for Function')
    print('2 for Functions comparison')
    print('3 for Graph crossing')
    print('4 for Power function')
    print('5 for Triangle check')
    print('6 for Sequence position check')
    print('7 for 10 order position check')
    run = input('...or "exit" to leave the program: ')
    print('')

    if run == '1':
        return function()
    elif run == '2':
        return comparison()
    elif run == '3':
        return graph()
    elif run == '4':
        return function_power()
    elif run == '5':
        return triangle()
    elif run == '6':
        return position()
    elif run == '7':
        return infinity()
    elif run == 'exit' or run == 'Exit':
        sys.exit()
    else:
        print('Wrong input, try again')


while True:
    runner()
    print('')
