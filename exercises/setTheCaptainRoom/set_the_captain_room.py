membersPerGroup = int(input())

roomNumberList = list(map(int, input().split()))

uniqueRoom = set(roomNumberList)

print(((sum(uniqueRoom)*membersPerGroup)-(sum(roomNumberList)))//(membersPerGroup-1))
