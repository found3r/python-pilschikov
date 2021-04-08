#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


zero_counter = 0
one_counter = 0
two_counter = 0
three_counter = 0
four_counter = 0
five_counter = 0
six_counter = 0
seven_counter = 0
eight_counter = 0
nine_counter = 0

amount = int(input('How many digits to generate: '))
for k in range(amount):
    number = random.randint(0, 9)
    if number == 0:
        zero_counter = zero_counter + 1
    elif number == 1:
        one_counter = one_counter + 1
    elif number == 2:
        two_counter = two_counter + 1
    elif number == 3:
        three_counter = three_counter + 1
    elif number == 4:
        four_counter = four_counter + 1
    elif number == 5:
        five_counter = five_counter + 1
    elif number == 6:
        six_counter = six_counter + 1
    elif number == 7:
        seven_counter = seven_counter + 1
    elif number == 8:
        eight_counter = eight_counter + 1
    elif number == 9:
        nine_counter = nine_counter + 1

print(max(one_counter, two_counter, three_counter, four_counter,
          five_counter, six_counter, seven_counter, eight_counter,
          nine_counter, zero_counter))