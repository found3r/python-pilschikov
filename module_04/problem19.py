#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

counter = 0
n = int(input('How many numbers to generate: '))
while n < 0:
    print('Wrong input, try again')
    n = int(input('How many numbers to generate: '))
while n != 0:
    a = random.randint(-1000, 1000)
    if a < 0:
        counter = counter + 1
    n = n - 1
print(f'There are {counter} negative numbers')