numberOfCommands = int(input())

queue = []

for x in range(numberOfCommands):

    query = list(map(int, input().split()))

    # enqueue
    if query[0] == 1:
        queue.append(query[1])

    # dequeue
    elif query[0] == 2:
        queue = queue[::-1]
        queue.pop()
        queue = queue[::-1]

    # element on front of the queue
    else:
        print(queue[0])
