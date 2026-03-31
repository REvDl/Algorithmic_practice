"""this function defines Hikoma number"""
def classify(number):
    if not isinstance(number,int):
        raise ValueError("not valid type")
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    my_num = [i for i in range(1, number) if number % i == 0]
    sum_of_divisors = sum(my_num)
    if sum_of_divisors == number:
        return "perfect"
    elif sum_of_divisors > number:
        return "abundant"
    else:
        return "deficient"