numberEnglish = int(input())

english = set(list(map(int, input().split())))

numberFrench = int(input())

french = set(list(map(int, input().split())))

print(len(english.difference(french)))
