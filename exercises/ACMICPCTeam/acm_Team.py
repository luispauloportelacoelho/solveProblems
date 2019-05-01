from itertools import combinations

def acmTeam(topic):

    positions = list(range(0, len(topic)))

    max_value = 0
    number_of_max = 0

    unorderedPairGenerator = combinations(positions, 2)

    for pair in unorderedPairGenerator:

        list1 = list(topic[pair[0]])
        list2 = list(topic[pair[1]])

        list1_size = len(list1)

        pair_value = 0

        for x in range(list1_size):
            if list1[x] == '1' or list2[x] == '1':
                pair_value += 1

        if pair_value == max_value:
            number_of_max += 1
        elif pair_value > max_value:
            max_value = pair_value
            number_of_max = 1

    return [max_value, number_of_max]
