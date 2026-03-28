import math
def score(x=int, y=int):
    distance = math.sqrt(pow(x, 2) + pow(y, 2))
    if distance > 10:
        return 0
    elif 5 < distance <= 10:
        return 1
    elif 1 < distance <=5:
        return 5
    return 10