m_size = int(input())
M = list(map(int, input().split()))
mSet = set(M)

n_size = int(input())
N = list(map(int, input().split()))
nSet = set(N)

differenceMSet = mSet.difference(nSet)
differenceNSet = nSet.difference(mSet)

unionDifferences = differenceMSet.union(differenceNSet)
