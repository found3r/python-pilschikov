#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)

import math
import sys


def functions():  # Derivative of 'x ^ x = a'

    x = 1
    a = int(input('Input "a" (a > 0) variable: '))
    if a < 0:
        a = int(input('"a" should be > 0, input "a" variable: '))
    while x != math.pow(a, 1 / x):
        if x == math.pow(a, 1 / x):
            x = math.pow(a, 1 / x)
        else:
            x = x + 1
    print('')
    print(f'Derivative of function = {x}*{x}^{x - 1}')

    # Root of 'ln(ctg[x] - 1) = a'

    print('')
    print(f'Function root = {math.pow(math.atan(math.exp(a) + 1), -1)}')


def average_geometric():  # Average geometric of three numbers

    number1 = int(input('Input first number: '))
    number2 = int(input('Input second number: '))
    number3 = int(input('Input third number: '))

    print('')
    print(f'Average geometric = '
          f'{pow(number1 * number2 * number3, 1 / 3) % 1}')


def rad():  # Circle and sphere length, square and volume

    radius = int(input('Input radius (mm): '))
    print('')
    print(f'Circle length: {round(2 * math.pi * radius, 2)} mm')
    print(f'Circle square: {round(math.pi * radius ** 2, 2)} mm^2')
    print(f'Circle volume: {round(4 / 3 * math.pi * radius, 2)} mm^3')


def rectangle():  # Perimeter and square of a triangle with two input cathets

    cathet1 = int(input('Input first cathet: '))
    cathet2 = int(input('Input second cathet: '))

    print(f'Square of rectangular triangle = {cathet1 * cathet2 / 2}')
    print(f'Perimeter of rectangular triangle = '
          f'{cathet1 + cathet2 + math.sqrt(cathet1 * cathet2)}')


def coord_triangle():  # Triangle perimeter and square based on three input coordinates

    x1 = int(input('Input x1 coordinate: '))
    y1 = int(input('Input y1 coordinate: '))
    x2 = int(input('Input x2 coordinate: '))
    y2 = int(input('Input y2 coordinate: '))
    x3 = int(input('Input x3 coordinate: '))
    y3 = int(input('Input y3 coordinate: '))
    print('')

    d1 = (x2 - x1) ^ 2 + (y2 - y1) ^ 2
    d2 = (x3 - x2) ^ 2 + (y3 - y2) ^ 2
    d3 = (x1 - x3) ^ 2 + (y1 - y3) ^ 2
    perimeter = d1 + d2 + d3
    hp = (d1 + d2 + d3) / 2  # Half of triangle perimeter
    # hp abbreviate used not to overfill next lines

    print(f'Triangle perimeter = {perimeter}')
    print(f'Triangle square = {math.sqrt(hp * (hp - d1) * (hp - d2)) * (hp - d3)}')


def runner():
    print('Type for available functions: ')
    print('1 for Functions')
    print('2 for Geometric average of three numbers')
    print('3 for Length, square and volume based on input radius')
    print('4 for Rectangle triangle square and perimeter')
    print('5 for Triangle square and perimeter based on coordinates')
    run = input('...or "exit" to leave the program: ')

    if run == '1':
        return functions()
    elif run == '2':
        return average_geometric()
    elif run == '3':
        return rad()
    elif run == '4':
        return rectangle()
    elif run == '5':
        return coord_triangle()
    elif run == 'exit' or 'Exit':
        sys.exit()
    else:
        print('Wrong input, try again')


while True:
    runner()
    print('')
