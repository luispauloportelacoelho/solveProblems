def downToZero(n):

    moves = 0
    arr = []

    if n % 2 != 0:
        return n
    else:
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                arr.append(x)
                moves += 1
        return arr[moves - 1] + 1

def calculateMax(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a
