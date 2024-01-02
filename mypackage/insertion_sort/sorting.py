from random import randint
from timing_sort_algorithms import run_sorting_algorithm

ARRAY_LENGTH = 1000

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1
        
        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    print(f"first and last element of array: {array[0]}, {array[len(array) - 1]}")
    return array


array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

run_sorting_algorithm("insertion_sort", array)