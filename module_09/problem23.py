#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


rows_amount = 30
columns_amount = 20

array = []
for n in range(rows_amount):
    row = []
    for k in reversed(range(columns_amount)):
        row.append(random.randint(-100, 100))
    array.append(row)

first_element_list = []
for n in range(rows_amount):
    first_element_list.append(array[n][0])
first_element_list.sort()

for n in range(rows_amount):
    