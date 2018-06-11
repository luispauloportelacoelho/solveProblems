def activityNotifications(expenditure, d):

    numberAlerts = 0

    if (d // 2 == 0):
        typeOfMedian = True
        position = d / 2
    else:
        typeOfMedian = False
        position = (d / 2) - 0.5

    size = len(expenditure) - 1

    sortSubArray, saveOrder = sortFirstTime(expenditure[0:d])

    for x in range(d, size):

        if x != d:
            sortSubArray, saveOrder = buildNewSubArray(sortSubArray, saveOrder,
                                                       x, expenditure[x], d)

        median = calculateMedian(sortSubArray, typeOfMedian, int(position))

        if expenditure[x] >= (median * 2):
            numberAlerts += 1

    return numberAlerts


def calculateMedian(sortSubArray, typeOfMedian, position):

    if typeOfMedian:
        return ((sortSubArray[position] + sortSubArray[position - 1]) / 2)
    else:
        return sortSubArray[position]


def sortFirstTime(subArray):
    sortSubArray = sorted(subArray)
    saveOrder = sorted(range(len(subArray)), key=lambda k: subArray[k])

    return sortSubArray, saveOrder


def buildNewSubArray(sortSubArray, saveOrder, x, value, d):

    iterations = d - 1

    savePosition = 0

    for k in range(0, iterations):
        if saveOrder[k] == 0:
            sortSubArray.remove(sortSubArray[k])
            saveOrder.remove(saveOrder[k])
        else:
            saveOrder[k] = saveOrder[k] - 1
            if k != 0 and value >= sortSubArray[k - 1] and value < sortSubArray[k]:
                savePosition = k

    if savePosition == 0:
        maxValue = max(sortSubArray)
        minValue = min(sortSubArray)

        if value >= maxValue:
            sortSubArray.append(value)
            saveOrder.append(iterations)
        elif value <= minValue:
            vectorAux = [value]
            vectorAux.append(sortSubArray)
            sortSubArray = vectorAux
            saveOrderAux = [iterations]
            saveOrderAux.append(saveOrder)
            saveOrder = saveOrderAux
    else:
        newArray = sortSubArray[0:savePosition]
        newArray.append(value)
        newArray.append(sortSubArray[savePosition:])
        saveOrderAux = saveOrder[0:savePosition]
        saveOrderAux.append(iterations)
        saveOrderAux.append(saveOrder[savePosition:])

        sortSubArray = newArray
        saveOrder = saveOrderAux

    return sortSubArray, saveOrder
