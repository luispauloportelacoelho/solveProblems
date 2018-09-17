from math import sqrt
def downToZero(n):

    memoize = set()
    count = 0

    queue = []
    queue.append((n, count))

    while len(queue):
        data, count = queue.pop(0)
        if data <= 1:
            if data == 1:
                count += 1
            break

        if data - 1 not in memoize:
            memoize.add(data - 1)
            queue.append((data - 1, count + 1))

        sqr = int(sqrt(data))

        for i in range(sqr, 1, -1):
            if data % i == 0:
                div = max(int(data/i), i)
                if div not in memoize:
                    memoize.add(div)
                    queue.append((div, count + 1))

    return count
