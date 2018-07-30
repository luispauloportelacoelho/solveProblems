def arrayManipulation(n, queries):
    newArray = [0] * n

    sizeQueries = len(queries)

    maxNumber = 0
    auxArray = [0] * n

    for x in range(sizeQueries):
        auxArray = [0] * n
        auxArray[(queries[x][0]-1): queries[x][1]] = [queries[x][2]] * (queries[x][1] + 1 - queries[x][0])

        newArray = [(x + y) for x, y in zip(newArray, auxArray)]

    return max(newArray)
