def circularArrayRotation(a: list, k: int, queries: list) -> list:

    lenA = len(a)

    if k > lenA:
        newK = int((k/lenA - int(k/lenA)) * lenA)

        if newK == 0:
            newK = 1
    else:
        newK = k

    newArray = a[lenA-newK:]

    newArray.extend(a[0:lenA-newK])

    response = []

    for x in queries:
        response.append(newArray[x])

    return response
