#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


rows_amount = 4
columns_amount = 7
row_index = int
column_index = int

array = []
for n in range(rows_amount):
    row = []
    for k in reversed(range(columns_amount)):
        row.append(random.randint(-20, 20))
    array.append(row)

print(array)

maximum_per_row = []

for n in range(rows_amount):
    maximum_per_row.append(max(array[n]))

max_element = max(maximum_per_row)

for n in range(rows_amount):
    for k in range(columns_amount):
        if array[n][k] == max_element:
            row_index = n
            column_index = k

print(f'Max element = {max_element}')
print(f'Row = {row_index + 1}')
print(f'Column = {column_index + 1}')


container = array[row_index]
array.remove(container)
container.sort()
array.insert(0, container)

for n in range(rows_amount):
    print(*array[n])
