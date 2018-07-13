import cmath

def transformation(complexInput):
    r = abs(complexInput)
    ph = cmath.phase(complexInput)
    print(r)
    print(ph)


if __name__ == '__main__':
    complexInput = complex(input())
    transformation(complexInput)
