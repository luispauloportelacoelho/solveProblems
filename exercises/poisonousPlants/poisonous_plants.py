def poisonousPlants(p: list) -> int:

    #if p == sorted(p):
    #    return 1

    numberPlants = len(p)
    p.append(-1)
    days = 1

    stack = []

    #while i < numberPlants:

    for i in range(0, numberPlants):
        if p[i] < p[i + 1]:
            stack.append(p[i+1])

        if stack and i == numberPlants - 1:
            return days + poisonousPlants(stack)


    return days - 1
