def countingValleys(n, s):
    start_position = 0
    total = 0
    valleys = 0
    block = False

    for x in range(0, n):
        if s[x] == 'D':
            total -= 1
        elif s[x] == 'U':
            total += 1

            if total == 0:
                block = False

        if total < 0 and not(block):
            valleys +=1
            block = True

    return valleys
