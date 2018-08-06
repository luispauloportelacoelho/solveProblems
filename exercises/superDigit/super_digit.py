def superDigit(n, k):

    if int(n) >= 1 and int(n) <= 9:
        return int(n)
    else:

        array = list(map(int, str(n)))

        arraySum = sum(array) * k

        return superDigit(arraySum, 1)
