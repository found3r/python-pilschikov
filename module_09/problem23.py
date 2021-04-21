#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random


rows = 30
columns = 20


def array_generator(rows_amount, columns_amount):  # Creates an array based on amount of
    # rows and columns
    array = []
    for n in range(rows_amount):
        row = []
        for _ in reversed(range(columns_amount)):
            row.append(random.randint(-10000, 10000))
        array.append(row)

    return array


def first_element_sort(rows_amount, array):  # Sorts array based on uprising first elements
    first_element_list = []  # List of first elements
    first_element_index_list = []  # Sorted list of indexes of first elements
    first_element_list_sorted = []  # List of uprising first elements
    for n in range(rows_amount):  # Creates two identical lists
        first_element_list.append(array[n][0])
        first_element_list_sorted.append(array[n][0])

    first_element_list_sorted.sort()
    for first_element in first_element_list_sorted:  # Lists indexes based on sorted
        # and unsorted lists
        first_element_index_list.append(first_element_list.index(first_element))

    array_sorted_first_element = []  # Array sorted based on uprising first elements
    for n in first_element_index_list:
        array_sorted_first_element.append(array[n])

    print('Array sort based on uprising first elements: \n')
    for n in range(rows_amount):
        print(*array_sorted_first_element[n])
    print('\n')


def sum_sort(rows_amount, columns_amount, array):
    sums_list = []  # List of row elements sums
    sums_list_sorted = []  # Sorted list of row elements sums
    row_index_list = []  # List of indexes based on sorted sum list
    for n in range(rows_amount):
        row_sum = 0
        for k in range(columns_amount):
            row_sum = row_sum + array[n][k]
        sums_list.append(row_sum)
        sums_list_sorted.append(row_sum)

    sums_list_sorted.sort()
    for n in sums_list_sorted:  # Sorts the indexes based on sums
        row_index_list.append(sums_list.index(n))

    print('Array sort based on uprising sums of elements of rows: \n')
    for n in row_index_list:
        print(*array[n])
    print('\n')


def max_element_sort(rows_amount, array):
    max_elements_list = []
    max_elements_list_sorted = []
    max_elements_index_list = []
    for n in range(rows_amount):
        max_elements_list.append(max(array[n]))
        max_elements_list_sorted.append(max(array[n]))

    max_elements_list_sorted.sort()
    for max_element in max_elements_list_sorted:
        max_elements_index_list.append(max_elements_list.index(max_element))

    print('Array sort based on uprising elements of each row:\n')
    for n in max_elements_index_list:
        print(*array[n])
    print('\n')


first_element_sort(rows, array_generator(rows, columns))
sum_sort(rows, columns, array_generator(rows, columns))
max_element_sort(rows, array_generator(rows, columns))
