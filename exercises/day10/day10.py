def countOne(n):
    binaryString = '{0:b}'.format(n)

    sizeBinaryString = len(binaryString)
    possibleSequence = False
    countOneTimes = 0
    countMaxOne = 0

    for x in range(0, sizeBinaryString):
        if binaryString[x] == "1" and not(possibleSequence):
            possibleSequence = True
            countOneTimes += 1
        elif binaryString[x] == "1" and possibleSequence:
            countOneTimes += 1
            if x == sizeBinaryString - 1 and countOneTimes > countMaxOne:
                countMaxOne = countOneTimes

        elif binaryString[x] == "0" and possibleSequence:
            possibleSequence = False
            countMaxOne = countOneTimes
            countOneTimes = 0

    return countMaxOne
