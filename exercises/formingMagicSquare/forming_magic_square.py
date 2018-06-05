def forming_magic_square(s):

    dim = len(s)

    count = 0
    saveResultLine = []
    saveResultCoumn = []
    for i in range(dim):
        t1 = 0
        t2 = 0
        for j in range(dim):
            t1 += s[i][j]
            t2 += s[j][i]
        saveResultLine.append(t1)
        saveResultCoumn.append(t2)

    t = 0
    for i in range(dim):
        t += s[i][i]

    saveResult = []
    saveResult.append(t)

    return saveResult


print(forming_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
