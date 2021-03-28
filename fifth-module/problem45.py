#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

a = int
counter = 0
sign_swap = 0
numbers_list = []

while a != 0:
    counter = counter + 1
    a = random.randint(-100, 100)
    numbers_list.append(a)

for i in range(1, counter):
    if (numbers_list[i] > 0) and (numbers_list[i - 1] < 0):
        sign_swap = sign_swap + 1
    elif (numbers_list[i - 1] > 0) and (numbers_list[i] < 0):
        sign_swap = sign_swap + 1

print(f'Sign changed {sign_swap} times')
