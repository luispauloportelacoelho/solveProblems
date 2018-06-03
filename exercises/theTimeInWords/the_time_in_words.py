def timeInWords(h, m):

    hour = convertHour(h, m)

    minutes = convertMinutes(m)

    return responseStructure(hour, minutes, h, m)


def convertHour(h, m):
    hours = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve"]

    if m > 30:
        return hours[h + 1]
    else:
        return hours[h]


def convertMinutes(m):

    if m == 30:
        return "half past"
    elif m == 0:
        return "o' clock"
    else:
        return convertMinutes_x(m)


def convertMinutes_x(m):

    units = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]

    decimals = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "ninteen"]

    if m > 30:
        m = 60 - m

    decimal = m // 10
    uni = m % 10

    if decimal == 2:
        minutes = "twenty"

        if uni != 0:
            minutes = minutes + " " + units[uni] + " minutes"

    elif decimal == 1:
        minutes = decimals[uni] + " minutes"

    else:
        minutes = units[uni] + " minutes"

    return minutes


def responseStructure(hour, minutes, h, m):
    if minutes == "o' clock":
        return hour + " " + minutes
    elif minutes == "half past":
        return minutes + " " + hour
    elif m < 30:
        if m == 15:
            return "quarter" + " past " + hour
        else:
            return minutes + " past " + hour
    elif m > 30:
        if m == 45:
            return "quarter" + " to " + hour
        else:
            return minutes + " to " + hour


print(timeInWords(1, 1))
#print(2%10)
