def minimumDistances(a: list) -> int:
    min_value = -1
    calc = 0
    exist_min = False

    for x in range(0, len(a)):
        if a[x] in a[(x+1):]:
            calc = abs(x - (a[(x+1):].index(a[x]) + x + 1))
            exist_min = True

        if min_value == -1 and exist_min:
            min_value = calc
        elif calc < min_value:
            min_value = calc

    return min_value
