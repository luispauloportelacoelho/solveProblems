def saveThePrisoner(prisoners: int, sweets: int, start_postion: int) -> int:

    warn = sweets + start_postion - 1

    if warn <= prisoners:
        return sweets + start_postion - 1
    elif warn > prisoners:

        first_group = prisoners - start_postion + 1

        complete = sweets - first_group

        factor = complete // prisoners

        position = complete - factor * prisoners

        if position == 0 and prisoners != start_postion:

            return start_postion + 1
        elif position == 0 and prisoners == start_postion:
            return start_postion
        else:
            return position



        #factor = sweets // prisoners

        #if (sweets % prisoners) != 0:
        #    return sweets + start_postion - 1 - factor * prisoners
        #else:
        #     return sweets + start_postion - 1 - (factor - 1) * prisoners
