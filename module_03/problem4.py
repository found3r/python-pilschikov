#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


number1 = int(input('Input the first number: '))
number2 = int(input('Input the second number: '))
number3 = int(input('Input the third number: '))
if (number1 % 2) == (number2 % 2) == (number3 % 2):
    print('true')
else:
    print('false')