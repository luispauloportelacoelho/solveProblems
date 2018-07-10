def solution(A):
    sol = 1

    newArray = set(A)

    if min(newArray) <= 0 and max(newArray) <= 0:
        return sol
    else:
        while sol in newArray:
            sol += 1
        return sol
