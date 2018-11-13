def quickSort(arr):
    pivot = arr[0]

    left = []
    right = []

    for x in range(1, len(arr)):
        if arr[x] < pivot:
            left.append(arr[x])
        elif arr[x] > pivot:
            right.append(arr[x])

    left.append(pivot)

    finalArray = left + right

    return finalArray
