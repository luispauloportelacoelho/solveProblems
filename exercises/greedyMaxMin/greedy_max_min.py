def maxMin(k: int, arr: list) -> int:

    sort_arr = sorted(arr)

    result = -1

    for x in range(0, len(sort_arr)-k+1):
        difference = sort_arr[k+x-1] - sort_arr[x]

        if x == 0:
            result = difference

        if result > difference:
            result = difference

    return result
