#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
intervals = ['unison', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh']


def interval(note_1_string, note_2_string):  # Finds the interval length
    note_1 = notes.index(note_1_string)  # Returns the integer of position from notes
    note_2 = notes.index(note_2_string)
    int_length = int(math.fabs(note_1 - note_2))  # Finds the length between notes
    int_position = int_length  # Position of the interval in list
    print(f'The interval is {intervals[int_position]}')


print('Available notes: C, D, E, F, G, A, B')
first_note = input('Input the first note: ')
second_note = input('Input the second note: ')
interval(first_note, second_note)
