import heapq

def runningMedian(a):

    lenA = len(a)

    medianArr = []

    selectValue = []

    countHeapSize = 0

    for x in a:
        heapq.heappush(selectValue, x)
        heapq.heapify(selectValue)

        print(selectValue)

        countHeapSize += 1

        calc = int(countHeapSize / 2)

        if countHeapSize % 2 == 0:
            medianVal = (selectValue[calc] + selectValue[calc - 1])/2
            medianArr.append(medianVal)
        else:
            medianArr.append(selectValue[calc])

    return medianArr


    return 1
