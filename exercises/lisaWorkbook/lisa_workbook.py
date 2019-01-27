def workbook(n: int, k: int, arr: list) -> int:
    special_pages = 0

    pages = 0

    value_max = max(arr)

    for x in range(0, len(arr)):

        if arr[x] > k:
            pages_necessary = arr[x] // k

            if (arr[x] % k) != 0:
                pages_necessary += 1
        else:
            pages_necessary = 1

        if pages_necessary == 1:
            pages += 1

            if pages <= arr[x]:
                special_pages += 1

        else:
            for y in range(0, pages_necessary):
                pages += 1

                if pages > y * k and pages <= (y+1) * k and arr[x] >= pages:

                    special_pages +=1

        if value_max < pages:
            break

    return special_pages

print(workbook(5, 3, [4, 2, 6, 1, 10]))

print(workbook(25, 10, [1, 29, 94, 15, 87, 100, 20, 55, 100, 45, 82, 80, 100, 100, 3, 53, 100, 2, 100, 100, 100, 100, 100, 100, 1]))
