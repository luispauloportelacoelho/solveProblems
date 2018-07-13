def average(array):
    # your code goes here

    newArray = set(array)

    sizeArray = len(newArray)

    count = 0

    for x in newArray:
        count += x

    total = count / sizeArray

    return total
