def runningMedian(a):
    #
    # Write your code here.
    #
    lenA = len(a)

    medianArr = []

    minHeap = []
    maxHeap = []
    minHeapSize = 0
    maxHeapSize = 0

    countHeapSize = 0

    for x in range(lenA):
        print("#####")
        if x == 0:
            heapq.heappush(minHeap, a[x])
            calc = a[x]
            minHeapSize += 1
        else:
            if a[x] < calc:
                maxHeapSize += 1
            else:
                minHeapSize += 1

            differenceHeapSize = abs(minHeapSize - maxHeapSize)

            if differenceHeapSize == 2 and minHeapSize < maxHeapSize:
                heapq.heappush(minHeap, -1 * heapq.heapreplace(maxHeap, -1 * a[x]))

                maxHeapSize -= 1
                minHeapSize += 1

            elif differenceHeapSize == 2 and minHeapSize > maxHeapSize:
                heapq.heappush(maxHeap, -1 * heapq.heapreplace(minHeap, a[x]))

                maxHeapSize += 1
                minHeapSize -= 1
            elif a[x] < calc:
                heapq.heappush(maxHeap, -1 * a[x])
            else:
                heapq.heappush(minHeap, a[x])

            differenceHeapSize = abs(minHeapSize - maxHeapSize)

            if differenceHeapSize == 0:
                calc = (-1 * maxHeap[0] + minHeap[0]) / 2
            elif minHeapSize > maxHeapSize:
                calc = minHeap[0]
            elif minHeapSize < maxHeapSize:
                calc = -1 * maxHeap[0]

        medianArr.append(calc)

    return medianArr
