from collections import Counter

def pairs(k: int, arr: list) -> int:

    number_of_pairs = 0

    sorted_arr = sorted(arr)
    dict_arr = Counter(arr)

    for x in range(0, len(arr)):

        if (sorted_arr[x] + k) in dict_arr:
            number_of_pairs += 1

    return number_of_pairs
