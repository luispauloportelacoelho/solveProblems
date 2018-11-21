def beautifulTriplets(d: int, arr: list) -> int:

    number_beautiful_triplets = 0

    for x in range(0, len(arr)):
        count_d = 1
        calc = arr[x] + count_d * d
        while count_d < 3 and calc in arr:
            count_d += 1
            calc = arr[x] + count_d * d

        if count_d == 3:
            number_beautiful_triplets += 1

    return number_beautiful_triplets
