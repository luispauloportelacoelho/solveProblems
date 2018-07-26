deliveryDay = list(map(int, input().split()))

lastDay = list(map(int, input().split()))

fine = 0


if deliveryDay[0] == lastDay[0] and deliveryDay[1] == lastDay[1] and deliveryDay[2] == lastDay[2]:

    print(fine)
elif deliveryDay[1] == lastDay[1] and deliveryDay[2] == lastDay[2]:

    if deliveryDay[0] > lastDay[0]:
        difference = deliveryDay[0] - lastDay[0]

        fine = 15 * difference
        print(fine)
    else:
        print(0)

elif deliveryDay[2] == lastDay[2]:
    if deliveryDay[1] > lastDay[1]:
        difference = deliveryDay[1] - lastDay[1]

        fine = 500 * difference

        print(fine)
    else:
        print(0)
elif deliveryDay[2] < lastDay[2]:
    print(0)
else:
    fine = 10000
    print(fine)
