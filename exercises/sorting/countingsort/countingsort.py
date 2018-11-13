def countingSort(arr):
    array_of_positions = [0] * 100

    for x in arr:
        array_of_positions[x] = array_of_positions[x] + 1

    return array_of_positions
