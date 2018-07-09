def beautifulDays(i, j, k):
    days = []
    x = i
    while x <= j:
        days.append(x)
        x += 1

    sizeDays = len(days)

    beautiful = 0

    for ii in range(sizeDays):
        calc = abs(days[ii] - reverseNumber(days[ii]))

        if (calc % k) == 0:
            beautiful += 1

    return beautiful


def reverseNumber(n):
    return int(str(n)[::-1])
