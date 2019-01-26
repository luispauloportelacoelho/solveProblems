def catAndMouse(x: int, y: int, z: int) -> str:

    diff_catA_mouse = abs(x - z)
    diff_catB_mouse = abs(y - z)

    if diff_catA_mouse == diff_catB_mouse:
        return 'Mouse C'
    elif diff_catA_mouse > diff_catB_mouse:
        return 'Cat B'
    elif diff_catA_mouse < diff_catB_mouse:
        return 'Cat A'
