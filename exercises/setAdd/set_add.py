numberCountry = int(input())

uniqueCountryList = set()

for x in range(numberCountry):
    newCountry = str(input())
    uniqueCountryList.add(newCountry)


print(len(uniqueCountryList))
