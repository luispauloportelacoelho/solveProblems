def dayProgrammer(year: int) -> str:

    if year == 1918:
        return '26.09.1918'

    if year > 1918:
        yearType = validateLeapYearGregorian(year)
    elif year < 1918:
        yearType = validateLeapYearJulian(year)

    if yearType is True:
        response = '12.09.' + str(year)

    elif yearType is False:
        response = '13.09.' + str(year)

    return response


def validateLeapYearGregorian(year: int) -> bool:

    leap = False

    if (year % 4) != 0:
        leap = False
    else:
        if (year % 100) == 0 and (year % 400) != 0:
            leap = False
        else:
            leap = True

    return leap

def validateLeapYearJulian(year: int) -> bool:
    leap = False

    if (year % 4) == 0:
        leap = True

    return leap
