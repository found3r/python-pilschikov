#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


print('Type a 3-digit number: ')
x = int(input())
check_if_correct_number = 0
while check_if_correct_number != 1:
    if x > 999:
        print('Incorrect number, please, type again: ')
        x = int(input())
    elif x < 100:
        print('Incorrect number, please, type again: ')
        x = int(input())
    else:
        print('Sum of number digits = ', x // 100 + x // 10 % 10 + x % 10)
        check_if_correct_number = check_if_correct_number + 1
