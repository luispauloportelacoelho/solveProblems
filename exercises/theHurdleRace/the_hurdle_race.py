def hurdleRace(k, height):
    maxHeight = max(height)

    if maxHeight > k:
        return maxHeight - k
    else:
        return 0    
