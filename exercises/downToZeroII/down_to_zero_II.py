def downToZero(n):

    count = n
    moves = 0
    mul = []

    for x in range(1, n//2+1):

        if n % x == 0:
            mul.append(x)

    #for x in range(len(mul)):



    while count > 0:

        count -= 1
        moves += 1

    return moves
