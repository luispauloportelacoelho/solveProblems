def largestRectangle(A: list) -> int:
    ans = 0
    A = [-1] + A

    A.append(-1)
    n = len(A)
    stack = [0]

    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h * (i - stack[-1] - 1)
            ans = max(ans, area)
        stack.append(i)
    return ans
