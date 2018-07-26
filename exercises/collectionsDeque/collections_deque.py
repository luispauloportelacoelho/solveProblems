from collections import deque

N = int(input())

d = deque()

for x in range(N):
    method_value = list(map(str, input().split()))

    if method_value[0] == "append":
        d.append(method_value[1])
    elif method_value[0] == "appendleft":
        d.appendleft(method_value[1])
    elif method_value[0] == "pop":
        d.pop()
    elif method_value[0] == "popleft":
        d.popleft()
    elif method_value[0] == "clear":
        d.clear()

for y in range(len(d)):
    print(d[y], end=" ")
