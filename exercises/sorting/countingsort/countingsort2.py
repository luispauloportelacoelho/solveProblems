def countingSort(arr):
    array_of_positions = [0] * 100

    sortArray = []

    for x in arr:
        array_of_positions[x] = array_of_positions[x] + 1

    for x in range(0, len(array_of_positions)):
        sortArray = sortArray + [x] * array_of_positions[x]

    return sortArray
