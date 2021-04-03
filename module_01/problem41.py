#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


print('Full circle is 360 degrees')
print('That makes a single hour equal ', 360, ' degrees')
print('And as there are 60 minutes in each hour each minute is ', 360 // 60, ' degree')
# hour_degrees_per_second = 360 // 60 // 12 / 60
hour_degrees_per_second = 360 / (60 * 60 * 12)
print('Which means that each second is about ', hour_degrees_per_second, ' degrees')
start_point = 0
print("Let's suppose that the begging of the day is ", start_point)
print('Type hours, minutes and seconds to find the difference between the begging and the current moment')
hours = int(input())
minutes = int(input())
seconds = int(input())
check_if_correct_number = 0
while check_if_correct_number != 1:
    if hours > 12:
        print('Incorrect number, try again: ')
        hours = int(input())
    if hours < 0:
        print('Incorrect number, try again: ')
        hours = int(input())
    else:
        check_if_correct_number = check_if_correct_number + 1
check_if_correct_number = 0
while check_if_correct_number != 1:
    if minutes > 60:
        print('Incorrect number, try again: ')
        minutes = int(input())
    if minutes < 0:
        print('Incorrect number, try again: ')
        minutes = int(input())
    else:
        check_if_correct_number = check_if_correct_number + 1
check_if_correct_number = 0
while check_if_correct_number != 1:
    if seconds > 60:
        print('Incorrect number, try again: ')
        seconds = int(input())
    if seconds < 0:
        print('Incorrect number, try again: ')
        seconds = int(input())
    else:
        check_if_correct_number = check_if_correct_number + 1
seconds_sum = hours * 3600 + minutes * 60 + seconds
print('The degrees difference is ', seconds_sum * hour_degrees_per_second % 360, ' degrees')
