def closestNumbers(arr: list) -> list:
    sortedArr = sorted(arr)

    absoluteDifference = 0

    save = []

    save.append(sortedArr[0])
    save.append(sortedArr[1])
    absoluteDifference = abs(sortedArr[0] - sortedArr[1])

    for x in range(1, len(arr)-1):
        difference = abs(sortedArr[x] - sortedArr[x+1])

        if difference == absoluteDifference:
            save.append(sortedArr[x])
            save.append(sortedArr[x+1])
        elif difference < absoluteDifference:
            save = []
            absoluteDifference = difference
            save.append(sortedArr[x])
            save.append(sortedArr[x+1])

    return save
