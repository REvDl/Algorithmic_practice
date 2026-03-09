import math


def is_prime(n: int):
	if n <= 0:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def divisors(integer: int):
	result = []
	if is_prime(integer):
		return f"{integer} is prime"
	for i in range(2, integer):
		if integer % i == 0:
			result.append(i)
	return result

print(divisors(13))