def convert(number):
    if not isinstance(number, int):
        raise TypeError
    stroka = ""
    if number % 3 == 0:
        stroka += "Pling"
    if number % 5 == 0:
        stroka += "Plang"
    if number % 7 == 0:
        stroka += "Plong"
    if not stroka:
        return str(number)
    return stroka