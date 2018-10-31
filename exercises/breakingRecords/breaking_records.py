def breakingRecords(scores: list) -> list:
    minScore = 0
    maxScore = 0
    countMinScore = 0
    countMaxScore = 0

    games = len(scores)

    for i in range(games):
        if i == 0:
            minScore = scores[i]
            maxScore = scores[i]
        else:
            if scores[i] > maxScore:
                maxScore = scores[i]
                countMaxScore += 1
            elif scores[i] < minScore:
                minScore = scores[i]
                countMinScore += 1



    result = [countMaxScore, countMinScore]

    return result
