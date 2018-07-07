def array_left_rotation(a, d):
    if len(a) == d:
        return a

    newArray = a[d:]

    newArray = newArray + a[0:d]

    return newArray
