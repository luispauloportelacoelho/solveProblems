import math

def find_angle(ab, bc):

    C = math.atan(ab / bc)

    a = 0.5 * (math.sqrt(ab*ab + bc*bc))

    b = bc

    c = math.sqrt(a*a + b*b - 2*a*b*math.cos(C))

    preTeta = math.acos((a*a - b*b - c*c)/(-2*b*c))

    teta = math.degrees(preTeta)
    teta = str(round(teta, 0)).split('.')[0]

    message = teta + '°'

    return message
