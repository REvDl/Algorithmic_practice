def square_root(number: int) -> int:
    if number <= 1:
        return number
    num = 0
    while num * num != number:
        num += 1
    return num



print(square_root(4))
