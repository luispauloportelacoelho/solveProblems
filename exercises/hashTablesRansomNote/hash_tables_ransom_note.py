def checkMagazine(magazine, note):

    repeat = {}
    for word in magazine:
        if not(word in repeat):
            repeat[word] = 1
        else:
            repeat[word] += 1

    answer = 'Yes'

    for i in range(len(note)):
        if not(note[i] in magazine) or (repeat[note[i]] == 0):
            answer = 'No'
            break
        else:
            repeat[note[i]] -= 1

    print(answer)
