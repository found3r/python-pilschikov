#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


array = []
for n in range(4):
    row = []
    for k in range(7):
        # row.append(random.randint(-20, 20))
        row.append(k)
    array.append(row)

print(array)

for n in range(6):
    if array[0][n] > array[0][n + 1]:
        

print(*array)