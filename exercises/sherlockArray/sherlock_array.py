def solve(a):
    # Complete this function
    message = 'NO'

    sizeA = len(a)

    if sizeA == 1:
        message = 'YES'
        return message
    elif sizeA == 2:
        return message

    rightSum = sum(a[2:])
    leftSum = a[0]

    for x in range(1, sizeA-1):
        if leftSum == rightSum:
            message = "YES"
            break
        else:
            leftSum += a[x]
            rightSum -= a[x+1]

    return message
