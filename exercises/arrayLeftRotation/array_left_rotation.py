def array_left_rotation(a, d):
    if len(a) == d:
        return a

    sizeA = len(a)

    newArray = a[d:sizeA]

    for i in range(d):
        newArray.append(a[i])

    return newArray
