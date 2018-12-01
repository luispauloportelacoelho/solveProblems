def getMinimumCost(k: int, c: list) -> int:

    price_sort = sorted(c, reverse=True)

    minimum_price = 0

    price_factor = 0

    for x in range(0, len(c)):
        if (x % k) == 0 and x != 0:
            price_factor += 1

        minimum_price += (price_factor + 1) * price_sort[x]

    return minimum_price
