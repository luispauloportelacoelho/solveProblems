from collections import Counter
import operator
def equalizeArray(arr):

    arrDict = Counter(arr)

    maxKey = max(arrDict.items(), key=operator.itemgetter(1))[0]

    return len(arr)-arrDict.get(maxKey)
