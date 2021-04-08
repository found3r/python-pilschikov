#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random
import math


x_list = []
y_list = []
difference_list = []

for n in range(20):
    x_number = random.randint(-1000, 1000)
    y_number = random.randint(-1000, 1000)
    x_list.append(x_number)
    y_list.append(y_number)

for k in range(20):
    delta = math.fabs(x_list[k] - y_list[k])
    difference_list.append(delta)

print(f'Longest distance = {max(difference_list)}')