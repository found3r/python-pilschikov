#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


def divide_by_zero(numerator, quotient):
    try:
        return numerator / quotient
    except ZeroDivisionError:
        print('Exception noticed')
        return 0


if True or divide_by_zero(1, 0) > 0:
    print('True')
else:
    print('False')
if divide_by_zero(1, 0) > 0 or True:
    print('True')
else:
    print('False')
