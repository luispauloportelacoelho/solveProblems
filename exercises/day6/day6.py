def separate(s):
    sizeS = len(s)

    odd = ""
    even = ""

    for i in range(0, sizeS):

        if (i % 2) == 0:
            odd = odd + s[i]
        else:
            even = even + s[i]

    return odd + " " + even


if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        s = str(input())
        print(separate(s))
