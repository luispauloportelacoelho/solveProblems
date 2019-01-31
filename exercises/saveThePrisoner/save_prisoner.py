def saveThePrisoner(prisoners: int, sweets: int, start_postion: int) -> int:

    last = (prisoners + sweets + start_postion - 1) % prisoners

    if last == 0:
        return prisoners
    else:
        return last
