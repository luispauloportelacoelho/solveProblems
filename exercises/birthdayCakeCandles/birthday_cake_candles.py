def birthdayCakeCandles(ar):
    sizeAr = len(ar)

    maxValue = max(ar)

    countMax = 0

    for i in range(sizeAr):
        if ar[i] == maxValue:
            countMax += 1

    return countMax
