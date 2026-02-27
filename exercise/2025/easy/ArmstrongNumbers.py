def is_armstrong_number(number):
    s = str(number)
    num_digits = len(s)
    sum_of_powers = 0
    for char_digit in s:
        sum_of_powers += int(char_digit) ** num_digits
    return sum_of_powers == number