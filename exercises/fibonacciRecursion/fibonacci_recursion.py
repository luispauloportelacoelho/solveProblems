def fib_recusion(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_recusion(n-1) + fib_recusion(n-2)
