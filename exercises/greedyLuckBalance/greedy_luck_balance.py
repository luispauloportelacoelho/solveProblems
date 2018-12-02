from operator import itemgetter


def luckBalance(k: int, contests: list) -> int:

    lena_luck = 0

    loses = 0

    contests_importance = sorted(contests, key=itemgetter(1))
    value_losses = []
    count = 0

    for x in range(0, len(contests)):
        if contests_importance[x][1] == 0:
            lena_luck += contests_importance[x][0]

        if loses == 0 and contests_importance[x][1] == 1:
            value_losses = sorted(contests_importance[x:], key=itemgetter(0), reverse=True)

        if (value_losses) and value_losses[count][1] == 1 and loses < k:
            lena_luck += value_losses[count][0]
            loses += 1
            count += 1
        elif (value_losses) and value_losses[count][1] == 1 and loses >= k:
            lena_luck -= value_losses[count][0]
            loses += 1
            count += 1

    return lena_luck
