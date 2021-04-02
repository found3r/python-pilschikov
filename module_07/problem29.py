#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


colours = ['green', 'red', 'yellow', 'white', 'black']
animals = ['rat', 'cow', 'tiger', 'hare', 'dragon', 'snake',
           'horse', 'sheep', 'monkey', 'chicken', 'dog', 'pig']


def japanese_calendar(year):
    year = year - 4
    cycle_year = year % 60  # Finds the exact year inside a cycle
    sub_cycle = cycle_year // 12   # Finds the cycle's number
    sub_cycle_year = cycle_year % 12  # Finds the exact year of a cycle
    year_colour = colours[sub_cycle]
    year_animal = animals[sub_cycle_year]
    print(f'This year was a year of the {year_colour} {year_animal}')


some_year = int(input('Input a year: '))
while some_year <= 0:
    print("Wrong input, year can't be less than zero")
    some_year = int(input('Input a year: '))

japanese_calendar(some_year)