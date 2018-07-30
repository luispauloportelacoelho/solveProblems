def countApplesAndOranges(s, t, a, b, apples, oranges):
    numberApples = len(apples)
    numberOranges = len(oranges)

    applesHouse = 0
    orangesHouse = 0

    for x in range(numberApples):
        position = a + apples[x]
        if position >= s and position <= t:
            applesHouse += 1

    print(applesHouse)

    for x in range(numberOranges):
        position = b + oranges[x]
        if position >= s and position <= t:
            orangesHouse += 1

    print(orangesHouse)
