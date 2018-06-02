def diagonalDifference(mat):

    difference = 0
    dimension = calculateSize(mat)

    diagonal_1 = 0
    diagonal_2 = 0

    for i in range(dimension):
        diagonal_1 += mat[i][i]

    for j in range(dimension):
        diagonal_2 += mat[j][dimension - 1 - j]

    difference = abs(diagonal_1 - diagonal_2)

    return difference


def calculateSize(mat):
    return len(mat)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
