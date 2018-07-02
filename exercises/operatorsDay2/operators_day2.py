def solve(meal_cost, tip_percent, tax_percent):
    totalCost = 0

    tip = meal_cost * (tip_percent / 100)

    tax = meal_cost * (tax_percent / 100)

    totalCost = meal_cost + tip + tax

    result = "The total meal cost is " + str(round(totalCost)) + " dollars."

    return result
