def array_reverse(A):
    sizeA = len(A) - 1

    newArray = ""
    for x in range(sizeA, -1, -1):
        if x == sizeA:
            newArray = "" + str(A[x])
        else:
            newArray = newArray + " " + str(A[x])

    return newArray
