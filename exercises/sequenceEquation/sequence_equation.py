def permutationEquation(p: list) -> list:

    lenP = len(p)

    y = []

    for x in range(1, lenP+1):

        k = p.index(x) + 1
        kk = p.index(k) + 1
        y.append(kk)

    return y
