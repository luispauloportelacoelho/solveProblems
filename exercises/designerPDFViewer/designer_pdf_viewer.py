def designerPdfViewer(h: list, word: str):

    word_array = list(word)
    word_int_array = []

    factor = 96

    max_value = 0

    for x in range(0, len(word_array)):
        position = ord(word_array[x]) - factor - 1

        if x == 0:
            max_value = h[position]
        elif h[position] > max_value:
            max_value = h[position]

    return max_value * len(word_array)
