'''Find the maximum element present in stack
It was used a list as a stack'''

numberOfCommands = int(input())

newStack = []

for x in range(numberOfCommands):

    query = list(map(int, input().split()))

    if query[0] == 1:
        newStack.append(query[1])
    elif query[0] == 2:
        newStack.pop()
    else:
        print(max(newStack))
