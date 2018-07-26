initialValue = list(map(int, input().split()))

arrayN = list(map(int, input().split()))

setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))

count = 0

for x in range(initialValue[0]):

    if arrayN[x] in setA:
        count += 1

    if arrayN[x] in setB:
        count -= 1

print(count)
