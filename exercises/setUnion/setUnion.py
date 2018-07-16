'''
Task
The students of District College have subscriptions to English and French
newspapers. Some students have subscribed only to English, some have subscribed
to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the
English newspaper, and the other set is subscribed to the French newspaper.
The same student could be in both sets. Your task is to find the total number
of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, numberEnglish, the number of students who
have subscribed to the English newspaper.
The second line contains english space separated roll numbers of those
students.
The third line contains an integer numberFrench, the number of students who
have subscribed to the
French newspaper.
The fourth line contains french space separated roll numbers of those students.
'''

numberEnglish = int(input())

english = set(list(map(int, input().split())))

numberFrench = int(input())

french = set(list(map(int, input().split())))

print(len(english) + len(french) - len(english.intersection(french)))
