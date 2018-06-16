import heapq

def activityNotifications(expenditure, d):
    numberAlerts = 0

    if (d // 2 == 0):
        typeOfMedian = True
        position = d / 2
    else:
        typeOfMedian = False
        position = (d / 2) - 0.5

    size = len(expenditure) - 1

    for x in range(d, size):
        median = calculateMedian(expenditure[(x - d):(x - 1)], typeOfMedian, int(position))

        if expenditure[x] >= (median * 2):
            numberAlerts += 1

    return numberAlerts


def calculateMedian(subArray, typeOfMedian, position):

    #sortSubArray = sorted(subArray)
    sortSubArray = sortHeap(subArray)
    print(sortSubArray)

    if typeOfMedian:
        return ((sortSubArray[position] + sortSubArray[position - 1]) / 2)
    else:
        return sortSubArray[position]


def sortHeap(subArray):

    sizeA = len(subArray)

    heap = []
    for x in range(0, sizeA):
        heapq.heappush(heap, subArray[x])

    heapq.heapify(heap)
    print(subArray)
    print(heap)
    print(heap[1])


    return heap

sortHeap([20, 3, 4, 2, 3, 6, 8, 4, 5])
