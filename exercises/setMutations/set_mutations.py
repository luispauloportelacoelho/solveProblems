if __name__ == '__main__':
    numberOfElementA = int(input())

    A = set(list(map(int, input().split())))

    numberOfOperations = int(input())

    for x in range(numberOfOperations):
        operation = list(map(str, input().split()))
        newSet = list(map(int, input().split()))

        if operation[0] == 'intersection_update':
            #Update the set by keeping only the elements found in it and an iterable/another set.
            A.intersection_update(newSet)
        elif operation[0] == 'update':
            #Update the set by adding elements from an iterable/another set.
            A.update(newSet)
        elif operation[0] == 'symmetric_difference_update':
            #Update the set by only keeping the elements found in either set, but not in both.
            A.symmetric_difference_update(newSet)
        elif operation[0] == 'difference_update':
            #Update the set by removing elements found in an iterable/another set.
            A.difference_update(newSet)

    calculate = sum(A)
    print(calculate)
