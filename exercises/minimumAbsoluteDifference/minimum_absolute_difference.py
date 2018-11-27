def minimumAbsoluteDifference(arr: list) -> int:
    len_arr = len(arr)

    min_value = 0

    for x in range(0, len_arr):
        for y in range(0, len_arr):

            if x == 0 and y == 1:
                min_value = abs(arr[x] - arr[y])

            if x != y:
                difference = abs(arr[x] - arr[y])

                if difference < min_value:
                    min_value = difference

    return min_value
