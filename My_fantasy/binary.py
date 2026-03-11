


def binary(n:int) -> str:
	number = []
	while n != 0:
		number.append(str(n % 2))
		n //= 2
	return "".join(reversed(number))






print(binary(10))