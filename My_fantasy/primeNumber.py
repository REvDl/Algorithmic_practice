



def prime_number(n:int) -> list[int]:
	start_number = 2
	numbers = []
	while n > 1:
		while n % start_number == 0:
			n = n / start_number
			numbers.append(start_number)
		start_number += 1
	return numbers




print(prime_number(945_871_26))