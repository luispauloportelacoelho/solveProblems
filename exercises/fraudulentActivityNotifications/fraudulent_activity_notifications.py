def activityNotifications(expenditure, d):

    numberAlerts = 0
    typeOfMedian = False

    if (d // 2 == 0):
        typeOfMedian = True
        postion = d / 2
    else:
        position = (d / 2) - 0.5

    for x in range(d, len(expenditure)):
        median = calculateMedian(expenditure[(x - d):(x - 1)], typeOfMedian, int(position))

        print("#####")
        print(expenditure[x])
        print(median)

        if expenditure[x] >= (median * 2):
            numberAlerts += 1

    return numberAlerts


def calculateMedian(subArray, typeOfMedian, position):

    sortSubArray = sorted(subArray)

    if typeOfMedian:
        return (sortSubArray[position] + sortSubArray[position - 1]) / 2
    else:
        return sortSubArray[position]
