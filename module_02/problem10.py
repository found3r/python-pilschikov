#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


x = int(input('Input "x" variable = '))
print(x)

if (x >= 0) and (x <= 1):
    print('Statement "a" is true')
else:
    print('Statement "б" is true')

if (x >= 2) and (x <= 5):
    print('Statement "в" is true')
elif (x >= -1) and (x <= 1):
    print('Statement "в" is true')
else:
    print('Statement "г" is true')

x = int(input('Input "x" variable for statements "д", "е" and "ж" = '))
y = int(input('Input "y" variable for statements "д", "е" and "ж" = '))
z = int(input('Input "z" variable for statements "д", "е" and "ж" = '))

if (x > 0) and (y > 0) and (z > 0):
    print('Statement "д" is true')
elif (x > 0) or (y > 0) or (z > 0):
    print('Statement "е" is true')
else:
    print('Statement "ж" is true')

year = int(input('Input year = '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('It is a leap year')
        else:
            print('It is not a leap year')
    else:
        print('It is not a leap year')
else:
    print('It is not a leap year')
