import heapq

#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #

    lenA = len(A)
    sweetness = 0

    heapq.heapify(A)

    count = 0

    while A[0] < k and len(A) > 1:

        min0 = heapq.heappop(A)
        min1 = heapq.heappop(A)

        heapq.heappush(A, min0 + 2 * min1)

        count += 1

    if A[0] < k:
        return -1
    else:
        return count
