def marcsCakewalk(calorie: list) -> int:
    min_miles = 0

    calorie = sorted(calorie, reverse=True)

    for x in range(0, len(calorie)):
        min_miles += calorie[x] * (2**x)

    return min_miles
