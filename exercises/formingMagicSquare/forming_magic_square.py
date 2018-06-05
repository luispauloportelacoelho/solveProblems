def forming_magic_square(s):

    dim = len(s)

    count = 0
    saveResult = []
    for i in range(dim):
        t = 0
        for j in range(dim):
            t += s[i][j]
        saveResult.append(t)

    t = 0
    for i in range(dim):
        t += s[i][i]

    saveResult.append(t)

    for i in range(dim):
        t = 0
        for j in range(dim):
            t += s[j][i]

        saveResult.append(t)

    return saveResult


print(forming_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
