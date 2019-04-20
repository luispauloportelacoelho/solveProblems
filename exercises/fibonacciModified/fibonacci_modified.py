def fibonacciModified(t1, t2, n):
    cache = {1: t1, 2: t2}

    def calculate(n):
        if n in cache:
            return cache[n]
        else:
            if n == 1:
                return t1
            elif n == 2:
                return t2
            else:
                cache[n] = calculate(n - 2) + calculate(n - 1)*calculate(n - 1)
                return cache[n]

    return calculate(n)
