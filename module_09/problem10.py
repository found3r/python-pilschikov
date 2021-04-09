#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

array = []
for n in range(4):
    row = []
    for k in reversed(range(7)):
        row.append(random.randint(-20, 20))
        # row.append(k)
    array.append(row)

print(array)

maximum_row = []
for n in range(4):
    maximum_row.append(max(array[n]))

maximum_column = max(maximum_row)
maximum_column_index = maximum_row.index(maximum_column)

print(array[maximum_column_index].index(maximum_column))
