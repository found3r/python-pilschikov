#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random
import math


multiplication = 1
n = int(input('How many numbers to generate: '))
while n < 0:
    print('Wrong input, try again')
    n = int(input('How many numbers to generate: '))
amount_container = n
while n != 0:
    a = random.randint(0, 1000)
    multiplication = multiplication * a
    n = n - 1

print(f'Average geometric = {round(math.pow(multiplication, 1 / amount_container), 4)}')