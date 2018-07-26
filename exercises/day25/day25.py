import math

iterations = int(input())

for x in range(iterations):
    valueToValidate = int(input())

    half = int(math.sqrt(valueToValidate)) + 1

    count = 0

    for y in range(2, half):
        if (valueToValidate % y) == 0:
            count = 1
            break

    if count == 1 or valueToValidate == 1:
        print("Not prime")
    else:
        print("Prime")
