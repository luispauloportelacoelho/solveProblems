def minimumAbsoluteDifference(arr: list) -> int:
    len_arr = len(arr)

    min_value = 0

    arr = sorted(arr)

    for x in range(1, len_arr):
        difference = abs(arr[x-1] - arr[x])

        if x == 1:
            min_value = difference
        elif x != 1 and difference < min_value:
            min_value = difference

    return min_value
