def staircase(n):
    numberSpace = n - 1
    space = " "
    numberStair = 1
    stair = "#"

    for x in range(0, n):
        conc = (space * numberSpace) + (stair * numberStair)
        numberSpace -= 1
        numberStair += 1
        print(conc)

    return True

print(staircase(4))
