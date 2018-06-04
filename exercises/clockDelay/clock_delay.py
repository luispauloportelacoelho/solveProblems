def clock_delay(h1, m1, h2, m2, k):
    t1 = convertToMinutes(h1, m1)

    t2 = convertToMinutes(h2, m2)

    t3 = convertToMinutes(k, 0)

    return t1 + t3 - t2


def convertToMinutes(h, m):
    return 60 * h + m
