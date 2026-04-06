def my_range_v1(*args):
	if len(args) == 1:
		stop = args[0]
		index = 0
		while index <= (stop - 1):
			yield index
			index += 1
	if len(args) == 2:
		start, stop = args[0], args[1]
		while start <= (stop - 1):
			yield start
			start += 1
	if len(args) == 3:
		start, stop, step = args[0], args[1], args[2]
		if step == 0:
			raise ValueError
		while (step > 0 and start < stop) or (step < 0 and start > stop):
			yield start
			start += step

def my_range(*args):
	if not args:
		raise TypeError("my_range expected at least 1 argument, got 0")
	start = args[0] if len(args) > 1 else 0
	stop = args[1] if len(args) > 1 else args[0]
	step = args[2] if len(args) == 3 else 1
	if step == 0:
		raise ValueError("step cannot be equal to zero")
	while (step > 0 and start < stop) or (step < 0 and start > stop):
		yield start
		start += step
# Тест-кейс 1: Только stop
print("Пример 1 (stop=5):", list(my_range(5)))
# Ожидаемый вывод: [0, 1, 2, 3, 4]

# Тест-кейс 2: start, stop и положительный шаг
print("Пример 2 (1, 10, 2):", list(my_range(1, 10, 2)))
# Ожидаемый вывод: [1, 3, 5, 7, 9]

# Тест-кейс 3: start, stop и отрицательный шаг
print("Пример 3 (10, 1, -2):", list(my_range(10, 1, -2)))
# Ожидаемый вывод: [10, 8, 6, 4, 2]


print("Пример 4 (ничего):", list(my_range_v1()))

