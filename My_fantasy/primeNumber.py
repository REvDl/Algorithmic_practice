



def prime_number(n:int) -> list[int]:
	start_number = 2
	numbers = []
	while n > 1:
		while n % start_number == 0:
			n = n / start_number
			numbers.append(start_number)
		start_number += 1
	return numbers


def task_two(n:int):
	storage = 1
	for i in range(1, n+1):
		if i % 2 == 0:
			print(f"{i}/{i + 1}")
			storage *= i / (i + 1)
		else:
			print(f"{i+1}/{i}")
			storage *= (i + 1) / i
	return round(storage, 2)



def task_three(x:int, e = 0.5*(10**-5)):
	n = 1
	total_sum = 0
	piece = ((-1) ** n) / (n * (x ** n))
	while abs(piece) > e:
		total_sum += piece
		n += 1
		piece = ((-1) ** n) / (n * (x ** n))
	return round(total_sum, 3)

# print(prime_number(945_871_26))
# print(task_two(10))
print(task_three(2))