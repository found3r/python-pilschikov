#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)

f"""
This problem solvation involves dependence on the first weekday
and prints the weekday referencing to the first weekday accordingly
"""

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
           'saturday', 'sunday']
first_weekday = input('Input the first weekday of the year: ')
while True:
    try:
        weekday.index(first_weekday)
    except ValueError:
        print('Wrong input, input should be done in lowercase and with full weekday name')
        first_weekday = input('Input the first weekday of the year: ')
    else:
        break

weekday_delta = weekday.index(first_weekday)
# Finds the difference between a year which starts with monday and
# the year starting with the {first_weekday}

print(f'The first weekday of this year is {first_weekday}')
year_day = int(input('Input day of the year: '))
while (year_day < 1) or (year_day > 365):
    print('Wrong day input, please, input again')
    year_day = int(input('Input day of the year: '))

day_finder = year_day % 7  # Finds the number of the day within the week
print(f'It is {weekday[day_finder - 1 + weekday_delta]}')
