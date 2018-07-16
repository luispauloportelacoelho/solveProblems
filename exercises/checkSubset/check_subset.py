numberTestCases = int(input())

for x in range(numberTestCases):

    numberElementsA = int(input())
    elementsA = set(list(map(int, input().split())))
    numberElementsB = int(input())
    elementsB = set(list(map(int, input().split())))

    print(bool(elementsA.issubset(elementsB)))
