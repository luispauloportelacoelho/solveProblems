def icecreamParlor(m, arr):
    lenArr = len(arr)

    result = []
    approve = False

    for x in range(0, lenArr):
        for y in range(0, lenArr):
            if x != y and (arr[x] + arr[y] == m):
                result.append(x + 1)
                result.append(y + 1)
                approve = True
                break

        if approve:
            break

    return result
