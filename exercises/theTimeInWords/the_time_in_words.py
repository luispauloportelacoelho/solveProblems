from num2words import num2words

def timeInWords(h, m):



    hour = convertHour(h)

    minutes = convertMinutes(m)

    return ""


def convertHour(h):
    hours = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    return hours[h]


def convertMinutes(m):

    m_max = 60

    if m == 30:
        return "half past"
    elif m == 0:
        return " o'clock"
    elif m > 30:
        minTo = m_max - m
        return num2words(minTo) + " minutes to "
    else:
        return num2words(m) + " minutes past "


def convertMinutes_x(m):

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    decimals = ["eleven", "twelve"]


    if m > 30:
        minTo = 60 - m
        decimal = minTo // 10
        uni = minTo % 10



#print(timeInWords(12, 3))
print(2%10)
