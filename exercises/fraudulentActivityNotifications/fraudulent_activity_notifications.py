import math
import os
import random
import re
import sys
import heapq

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    choose = round(d / 2)

    lenExpenditure = len(expenditure)

    arrayMedian = expenditure[0:d]
    arrayMedian.sort()

    minHeap = arrayMedian[choose:d]
    minHeapSize = len(minHeap)
    maxHeap = arrayMedian[0:choose]
    maxHeap = [x * (-1) for x in maxHeap]
    maxHeapSize = len(maxHeap)

    #heapq.heapify(minHeap)

    maxHeap.sort()

    if minHeapSize == maxHeapSize:
        firstMedian = (minHeap[0] - maxHeap[0]) / 2
    elif minHeapSize > maxHeapSize:
        firstMedian = minHeap[0]
    elif minHeapSize < maxHeapSize:
        firstMedian = -1 * maxHeap[0]

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

            if i < maxHeapSize:
                heapq._siftup(maxHeap, i)
                heapq._siftdown(maxHeap, 0, i)
        else:
            i = minHeap.index(valueToRemove)

            minHeap[i] = minHeap[-1]

            minHeap.pop()
            minHeapSize -= 1

            if i < minHeapSize:
                heapq._siftup(minHeap, i)
                heapq._siftdown(minHeap, 0, i)

        if minHeap[0] > expenditure[x]:
            heapq.heappush(maxHeap, -1 * expenditure[x])
            maxHeapSize += 1
        else:
            heapq.heappush(minHeap, expenditure[x])
            minHeapSize += 1

        if abs(minHeapSize - maxHeapSize) >= 2:
            if minHeapSize > maxHeapSize:
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))
                minHeapSize -= 1
                maxHeapSize += 1
            else:
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
                minHeapSize += 1
                maxHeapSize -= 1

        if minHeapSize == maxHeapSize and (expenditure[x] >= (minHeap[0] - maxHeap[0])):
            notifications += 1
        elif minHeapSize > maxHeapSize and expenditure[x] >= 2 * minHeap[0]:
            notifications += 1
        elif minHeapSize < maxHeapSize and expenditure[x] >= -2 * maxHeap[0]:
            notifications += 1

    return notifications


fptr = open('/Users/Luís Coelho/Desktop/Luis Coelho_20180321/Luís Coelho/Git/solveProblems/exercises/fraudulentActivityNotifications/fraudulent.txt', 'r')
n = (fptr.read().split("\n"))
v = n[0].split(" ")
v1 = n[1].split(" ")
v = list(map(int, v))
v1 = list(map(int, v1))

print(activityNotifications(v1, v[1]))

#n = int(nd[0])
#d = int(nd[1])

#expenditure = list(map(int, input().rstrip().split()))
fptr.close()
