import heapq

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    choose = int(d / 2)

    lenExpenditure = len(expenditure)

    arrayMedian = expenditure[0:d]
    arrayMedian.sort()

    minHeap = arrayMedian[choose:d]
    minHeapSize = len(minHeap)
    maxHeap = arrayMedian[0:choose]
    maxHeap = [x * (-1) for x in maxHeap]
    maxHeapSize = len(maxHeap)

    heapq.heapify(minHeap)
    heapq.heapify(maxHeap)

    if minHeapSize == maxHeapSize:
        firstMedian = (minHeap[0] - maxHeap[0]) / 2
    else:
        firstMedian = minHeap[0]

    notifications = 0
    countCycles = 0

    if expenditure[d] >= 2 * firstMedian:
        notifications += 1

    for x in range(d + 1, lenExpenditure):
        valueToRemove = expenditure[countCycles]
        countCycles += 1
        if minHeap[0] > valueToRemove:

            i = maxHeap.index(-1 * valueToRemove)

            maxHeap[i] = maxHeap[-1]

            maxHeap.pop()
            maxHeapSize -= 1

            if i < len(maxHeap):
                heapq._siftup(maxHeap, i)
                heapq._siftdown(maxHeap, 0, i)
        else:
            i = minHeap.index(valueToRemove)

            minHeap[i] = minHeap[-1]

            minHeap.pop()
            minHeapSize -= 1

            if i < len(minHeap):
                heapq._siftup(minHeap, i)
                heapq._siftdown(minHeap, 0, i)

        if minHeap[0] > expenditure[x-1]:
            heapq.heappush(maxHeap, -1 * expenditure[x-1])
            maxHeapSize += 1
        else:
            heapq.heappush(minHeap, expenditure[x-1])
            minHeapSize += 1

        #print('before update')
        #print(minHeap)
        #print(minHeapSize)
        #print(maxHeap)
        #print(maxHeapSize)
        if abs(minHeapSize - maxHeapSize) >= 2:
            if minHeapSize > maxHeapSize:
                #heapq.heappush(maxHeap, -1 * heapq.heapreplace(minHeap, a[x]))
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))
                minHeapSize -= 1
                maxHeapSize += 1
            else:
                #heapq.heappush(minHeap, -1 * heapq.heapreplace(maxHeap, -1 * a[x]))
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
                minHeapSize += 1
                maxHeapSize -= 1
        #print('after update')
        #print(minHeap)
        #print(maxHeap)

        if ((d % 2) == 0 and (expenditure[d] >= (minHeap[0] - maxHeap[0]))) or expenditure[d] >= 2 * minHeap[0]:
            notifications += 1

    print(notifications)

    return notifications
