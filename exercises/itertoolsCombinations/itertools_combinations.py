from itertools import combinations

#S = 'HACK 2'
S = list(input().split())

#s = 'HACK'
s = sorted(S[0])
#k = 2
k = int(S[1])

for j in range(1, k + 1):
    x = list(sorted(combinations(s, j)))
    sizeX = len(x)
    for i in range(sizeX):
        print(''.join(x[i]))
