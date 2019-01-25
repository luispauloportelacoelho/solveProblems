def getMoneySpent(keyboards: list, drives: list, money_to_spend: int) -> int:
    #
    # Write your code here.
    #
    keyboards_sort_price = sorted(keyboards)
    drivers_sort_price = sorted(drives)

    if (keyboards_sort_price[0] + drivers_sort_price[0] > money_to_spend):
        return -1
    else:
        possible_combinations = [(x,y) for x in keyboards_sort_price for y in drivers_sort_price]

        max_value = 0

        for x in range(0, len(possible_combinations)):
            possible_buy = possible_combinations[x][0] + possible_combinations[x][1]
            if possible_buy > max_value and possible_buy <= money_to_spend:
                max_value = possible_buy


        return max_value
