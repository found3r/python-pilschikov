#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)

import math

x = 1
power = -1
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

print('')
print(f'Function root = {math.pow(math.atan(math.exp(a) + 1), -1)}')

number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))
number3 = int(input('Input third number: '))

print('')
print(f'Average geometric = {pow(number1 * number2 * number3, 1 / 3) % 1}')

radius = int(input('Input radius (mm): '))
print('')
print(f'Circle length: {round(2 * math.pi * radius, 2)} mm')
print(f'Circle square: {round(math.pi * radius ** 2, 2)} mm^2')
print(f'Circle volume: {round(4 / 3 *  math.pi * radius, 2)} mm^3')