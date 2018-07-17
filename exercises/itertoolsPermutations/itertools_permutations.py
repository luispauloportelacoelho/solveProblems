from itertools import permutations

#S = 'HACK 2'
S = list(input().split())

#s = 'HACK'
s = S[0]
#k = 2
k = int(S[1])

#execute all combinations of k letters and sort
x = list(sorted(permutations(s, k)))
sizeX = len(x)
for i in range(sizeX):
    print(''.join(x[i]))
