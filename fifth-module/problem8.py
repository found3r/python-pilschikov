#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

numbers_list = []
a = 0
while a != 100:
    a = a + 1
    numbers_list.append(random.randint(-100000, 100000))
print(max(numbers_list) - min(numbers_list))
