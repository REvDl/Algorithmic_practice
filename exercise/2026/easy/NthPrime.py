"""nth_prime"""


def is_prime(num: int) -> bool:
	"function for helping main"
	if num < 2:
		return False
	for num_in_cycle in range(2, int(num ** 0.5) + 1):
		if num % num_in_cycle == 0:
			return False
	return True


def prime(number) -> int:
	"main function"
	if number == 0:
		raise ValueError("there is no zeroth prime")

	count = 0
	num = 2
	while count < number:
		if is_prime(num):
			count += 1
			if count == number:
				return num
		num += 1
	return 0


print(prime(1))
