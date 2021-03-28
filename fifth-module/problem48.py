#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


number = int(input('Input a positive number: '))
if number <= 0:
    while number <= 0:
        print('Wrong input')
        number = int(input('Input a positive number: '))

summary = 1
term_divisor = 2
container = number

while term_divisor <= number:
    while number % term_divisor == 0:
        number = number // term_divisor
        summary = summary + term_divisor
    term_divisor = term_divisor + 1

if summary == container:
    print('The number is perfect')
else:
    print('The number is not perfect')

