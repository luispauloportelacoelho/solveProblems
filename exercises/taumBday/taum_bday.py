def taumBday(b: int, w: int, bc: int, wc: int, z: int) -> int:

    normal = b * bc + w * wc
    calc_b = b * (wc + z) + w * wc
    calc_w = b * bc + w * (bc + z)

    array = [normal, calc_b, calc_w]

    return min(array)
