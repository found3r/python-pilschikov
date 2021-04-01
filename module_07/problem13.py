#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


seasons = ['winter', 'spring', 'summer', 'autumn']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
          'september', 'october', 'november', 'december']


def season_determinator(month):
    month_position = months.index(month)
    required_season = str
    if (month_position == 0) or (month_position >= 10):
        required_season = seasons[0]
    elif (month_position >= 1) and (month_position <= 3):
        required_season = seasons[1]
    elif (month_position >= 4) and (month_position <= 6):
        required_season = seasons[2]
    elif (month_position >= 7) and (month_position <= 9):
        required_season = seasons[3]

    print(f'The season is {required_season}')


stated_month = input('Input the month in lowercase: ')
while True:
    try:
        months.index(stated_month)
    except ValueError:
        print('Wrong input')
        stated_month = input('Input the month in lowercase: ')
    else:
        break

season_determinator(stated_month)
