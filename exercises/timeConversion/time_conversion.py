def time_conversion(time):

    hour = time[0:2]
    minute = time[3:5]
    second = time[6:8]
    time_format = time[8:]

    if time_format == "PM":
        hour = str(int(hour) + 12)

    return hour + ":" + minute + ":" + second
