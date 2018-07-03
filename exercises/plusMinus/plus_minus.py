def plusMinus(arr):
    sizeArr = len(arr)

    countPos = 0
    countNeg = 0
    countZero = 0

    for i in range(sizeArr):
        if arr[i] > 0:
            countPos += 1
        elif arr[i] < 0:
            countNeg += 1
        else:
            countZero += 1

    print(countPos/sizeArr)
    print(countNeg/sizeArr)
    print(countZero/sizeArr)

    return True

plusMinus([-4, 3, -9, 0, 4, 1])
