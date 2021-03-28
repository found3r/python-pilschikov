#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math

number = int(input('Input a number > 1: '))
if number <= 1:
    while number <= 1:
        print('Wrong input')
        number = int(input('Input a positive number: '))

log = int(math.log(number))
exp = int(math.exp(number))
summary = 0

for x in range(log, exp):
    summary = math.pow(x, 2)

print(f'Sum of squares in range from log to exp = {summary}')
