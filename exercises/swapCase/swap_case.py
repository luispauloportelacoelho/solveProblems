def swap_case(s):

    newMessage = ""

    for letter in s:
        if letter.islower():
            newMessage += letter.upper()
        elif not(letter.islower()):
            newMessage += letter.lower()
    return newMessage
