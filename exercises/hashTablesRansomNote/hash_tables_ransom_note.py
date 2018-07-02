def checkMagazine(magazine, note):

    repeat = {}

    answer = 'Yes'

    for i in range(len(note)):
        if not(note[i] in magazine) or (note[i] in repeat):
            answer = 'No'
            break
        else:
            repeat.update({note[i]: 1})

    print(answer)
