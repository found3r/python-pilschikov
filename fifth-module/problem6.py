#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math


number = int(input('Input any number: '))
k = 1
while math.fabs(number) % math.pow(10, k) != math.fabs(number):
     k = k + 1
print(f'There are {k} digits in the number')