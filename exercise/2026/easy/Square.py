def square_root(number: int) -> int:
    if number <= 1:
        return number
    num = 1
    while num * num != number:
        num += 1
    return num


def square_root_binary_search(number: int) -> int:
    """Returns a square root of a number using binary search for optimization"""
    if number <= 1:
        return number
    left, right = 1, number
    while left <= right:
        mid = (left + right) // 2
        product = mid * mid
        if product == number:
            return mid
        elif product < number:
            left = mid + 1
        else:
            right = mid - 1
    return 0





print(square_root(100))
print(square_root_binary_search(100))
