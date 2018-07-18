from collections import Counter

#A counter is a container that stores elements as dictionary keys, and their
#counts are stored as dictionary values.

numberOfShoes = int(input())
sizeShoes = list(input().split())
numberofCustomers = int(input())

sizeShoesQuant = Counter(sizeShoes)

listOfSizes = Counter(sizeShoesQuant).keys()

profit = 0

for x in range(numberofCustomers):

    S = list(input().split())

    if S[0] in listOfSizes and sizeShoesQuant.get(S[0]) > 0:
        sizeShoesQuant[S[0]] -= 1

        profit = profit + int(S[1])

print(profit)
