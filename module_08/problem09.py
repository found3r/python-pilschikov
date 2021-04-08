#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
           'saturday', 'sunday']
print('The first weekday of this year is monday')
year_day = int(input('Input day of the year: '))
while (year_day < 1) or (year_day > 365):
    print('Wrong day input, please, input again')
    year_day = int(input('Input day of the year: '))

day_finder = year_day % 7  # Finds the number of the day within the week
print(f'It is {weekday[day_finder - 1]}')
