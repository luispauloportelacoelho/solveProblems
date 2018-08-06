def chocolateFeast(n, c, m):

    # n money 6
    # c price 2
    # m embalagens 2

    chocolats = int(n / c)

    if m > chocolats:
        return chocolats
    elif (m/chocolats) == 1.0:
        return chocolats + 1
    else:
        special = chocolats

        while special >= m:
            chocolats += 1
            special = special - m + 1

        return chocolats
