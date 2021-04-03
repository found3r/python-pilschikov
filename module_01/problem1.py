#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math


def roman_to_arabic(arabic):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arab_val = 0
    for i in range(len(arabic)):
        if i > 0 and rom_val[arabic[i]] > rom_val[arabic[i - 1]]:
            arab_val += rom_val[arabic[i]] - 2 * rom_val[arabic[i - 1]]
        else:
            arab_val += rom_val[arabic[i]]
    return arab_val


def past_comma(number, digits_after_comma=0):
    return f'{number:.{digits_after_comma}f}'


def periodical_fraction(number, period, digits_after_comma):
    counter = 0
    number_storage = number
    while number % 1 != 0:
        number = number * 10
        counter = counter + 1
    number = number_storage
    periodical = str(number) + str(period)*(digits_after_comma-counter)
    return periodical


print('а) 5! = ', past_comma(math.factorial(5), 4))
print('б) LXIV = ', past_comma(roman_to_arabic('LXIV'), 4))
print('в) 6,38 = ', past_comma(6.38, 4))
print('г) -0,7(4) = ', periodical_fraction(-0.7, 4, 4))
print('д) 11/4 = ', past_comma(11 / 4, 4))
print('е) -1/6 = ', past_comma(-1 / 6, 4))
print('ж) sqrt(2) = ', past_comma(math.sqrt(2), 4))
print('п) = ', past_comma(math.pi, 4))
print('и) 5*10^6 = ', past_comma(5 * 10 ** 6, 4))
print('к) -24,8*10^(-7) = ', past_comma(-24.8 / 10 ** 7, 4))
print('л) 10^6 = ', past_comma(10 ** 6, 4))
print('м) 1/100000', past_comma(1 / 100000, 4))
