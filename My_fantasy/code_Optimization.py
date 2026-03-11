from functools import wraps
import time
def timer(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		execution_time = (end - start) * 1_000_000
		print(f"функция {func.__name__} выполнилась за {round(execution_time, 2)}MCS")
		return result
	return wrapper


@timer
def process_data(data, option=True):
	# Этап 1: Первичная обработка
	result = []
	for i in range(len(data)):
		if option:
			result.append(data[i] * 2)
		else:
			result.append(data[i] + 1)

	# Этап 2: Фильтрация по порогу
	tmp = []
	for i in range(len(result)):
		if result[i] > 10:
			tmp.append(result[i])

	# Этап 3: Нормализация
	final = []
	for i in range(len(tmp)):
		final.append(tmp[i] / 2)

	return final

@timer
def process_data_optimize(data:list[int], option:bool = True) -> list[int | float]:
	result = []
	for item in data:
		if option:
			result.append(item * 2)
		else:
			result.append(item + 1)
	filtration = []
	for item in result:
		if item > 10:
			filtration.append(item / 2)
	return filtration

@timer
def process_data_optimize_V2(data:list[int], option:bool = True) -> list[int | float]:
	if option:
		result = [x * 2 for x in data]
	else:
		result = [x + 1 for x in data]
	filtration = [item / 2 for item in result if item > 10]
	return filtration


arr = [1, 5, 10, 15, 20]
print(process_data(arr, True))
print(process_data_optimize(arr, True))
print(process_data_optimize_V2(arr, True))
