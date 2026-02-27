def square(number):
    if number > 64 or number < 1:
        raise ValueError('square must be between 1 and 64')
    square = 2 ** (number - 1)
    return square


def total():
    squeare_list = []
    for number in range(1, 65):
        square = 2 ** (number - 1)
        squeare_list.append(square)
    return sum(squeare_list)
