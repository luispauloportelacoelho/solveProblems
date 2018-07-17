class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = None

    def computeDifference(self):
        self.maximumDifference = abs(min(a) - max(a))

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
