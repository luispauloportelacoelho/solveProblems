'''Find the maximum element present in stack
It was used a list as a stack'''

numberOfCommands = int(input())

saveMax = []

for x in range(numberOfCommands):

    query = list(map(int, input().split()))

    if query[0] == 1:

        if len(saveMax) == 0:
            saveMax.append(query[1])
        elif query[1] < saveMax[-1]:
            saveMax.append(saveMax[-1])
        elif query[1] >= saveMax[-1]:
            saveMax.append(query[1])

    elif query[0] == 2:
        saveMax.pop()
    else:
        print(saveMax[-1])
