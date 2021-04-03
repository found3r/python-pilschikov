#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

a = int
numbers_list = []
while a != 0:
    a = random.randint(-100, 100)
    numbers_list.append(a)
minimal = min(numbers_list)
for i, x in enumerate(numbers_list):
    if x == minimal:
        print(f'Minimal number is in position {i + 1}')
