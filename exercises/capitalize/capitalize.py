def solve(s):

    transformation = ''

    for x in range(len(s)):

        if x == 0 or s[x-1] == ' ':
            if s[x].islower() and s[x].isalpha():
                transformation += s[x].upper()
            else:
                transformation += s[x]
        else:
            transformation += s[x]

    return transformation
