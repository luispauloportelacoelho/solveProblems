def acmTeam(topic):

    positions = list(range(0, len(topic)))

    max_value = 0

    save_values = []

    unorderedPairGenerator = ([x, y] for x in positions for y in positions if y > x)
    for pair in unorderedPairGenerator:

        list1 = list(topic[pair[0]])
        list2 = list(topic[pair[1]])

        list1_size = len(list1)

        pair_value = 0

        for x in range(list1_size):
            if list1[x] == '1' or list2[x] == '1':

                pair_value += 1

        save_values.append(pair_value)

    result = []

    max_value = max(save_values)

    result.append(max_value)

    result.append(save_values.count(max_value))

    return result
