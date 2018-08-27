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
                heapq.heappush(maxHeap, -1 * a[x])
                maxHeapSize += 1
            else:
                heapq.heappush(minHeap, a[x])
                minHeapSize += 1

            differenceHeapSize = abs(minHeapSize - maxHeapSize)

            print("======")
            print(differenceHeapSize)

            if differenceHeapSize == 2 and minHeapSize < maxHeapSize:
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))

                maxHeapSize -= 1
                minHeapSize += 1

            elif differenceHeapSize == 2 and minHeapSize > maxHeapSize:
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))

                maxHeapSize += 1
                minHeapSize -= 1

            differenceHeapSize = abs(minHeapSize - maxHeapSize)
            if differenceHeapSize == 0:
                calc = (-1 * maxHeap[0] + minHeap[0]) / 2
                print("----------------")
                print(-1 * maxHeap[0])
                print(minHeap[0])
            elif minHeapSize > maxHeapSize:
                print("^^^^^^^^^^^^^^^^")
                calc = minHeap[0]
            elif minHeapSize < maxHeapSize:
                print("~~~~~~~~~~~~~~~~")
                calc = -1 * maxHeap[0]

        print(calc)
        print(minHeap)
        print(maxHeap)

        medianArr.append(calc)

    return medianArr
