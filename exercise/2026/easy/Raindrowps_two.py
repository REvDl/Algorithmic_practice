def convert_(number):
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


DATA = {3: "Pling", 5: "Plang", 7: "Plong"}

def convert(number:int):
	result = ""
	for k, value in DATA.items():
		if number % k == 0:
			result += value
	return result or str(number)


def convert_three(number:int) -> str:
	result = "".join(v for k, v in DATA.items() if number % k == 0)
	return result or str(number)

print(convert(8))
