#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


total_elements = int(input('How many elements to print: '))
elements_per_row = int(input('How many elements should be on a single row: '))
counter = 0
numbers_list = []

for n in range(total_elements):
    number = random.randint(-10000, 10000)
    numbers_list.append(number)

for k in reversed(range(total_elements)):
    print(numbers_list[k], end=' ')
    counter = counter + 1
    if counter % elements_per_row == 0:
        print('')

