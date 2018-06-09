def activityNotifications(expenditure, d):

    numberAlerts = 0

    if (d // 2 == 0):
        typeOfMedian = True
        position = d / 2
    else:
        typeOfMedian = False
        position = (d / 2) - 0.5

    for x in range(d, len(expenditure) - 1):
        median = calculateMedian(expenditure[(x - d):(x - 1)], typeOfMedian, int(position))

        if expenditure[x] >= (median * 2):
            numberAlerts += 1

    return numberAlerts


def calculateMedian(subArray, typeOfMedian, position):

    sortSubArray = sorted(subArray)

    if typeOfMedian:
        return ((sortSubArray[position] + sortSubArray[position - 1]) / 2)
    else:
        return sortSubArray[position]
