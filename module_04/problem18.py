#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


counter = 0
container = -10000
while counter != 50:
    a = int(input('Input a number: '))
    if a > container:
        container = a
    counter = container + 1
print(f'The largenst number is {container}')
