def aVeryBigSum(ar):
    """Sum the elements in array."""
    size_ar = len(ar)

    sum = 0

    for i in range(size_ar):
        sum += ar[i]

    return sum


print(aVeryBigSum([5, 2, 3, 5, 5]))
