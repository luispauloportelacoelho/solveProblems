def max_hourglass(A):
    sizeA = len(A) - 2

    summaryCalculation = []

    for y in range(sizeA):
        for x in range(sizeA):
            calcIteration = 0
            calcIteration = A[y][x] + A[y][x+1] + A[y][x+2] + A[y+1][x+1] + A[y+2][x] + A[y+2][x+1] + A[y+2][x+2]

            summaryCalculation.append(calcIteration)

    return max(summaryCalculation)
