steps = int(input())

heap = []

minValue = 0

for x in range(steps):
    ite = list(map(int, input().split()))

    if ite[0] == 1:
        heapq.heappush(heap, ite[1])
    elif ite[0] == 2:
        if ite[1] == heap[0]:
            heapq.heappop(heap)
        else:
            i = heap.index(ite[1])

            heap[i] = heap[-1]
            heap.pop()
            if i < len(heap):
                heapq._siftup(heap, i)
                heapq._siftdown(heap, 0, i)
    else:
        print(heap[0])
