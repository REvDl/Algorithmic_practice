def digital_root(n):
	digits = [n // 10 ** i % 10 for i in range(len(str(n)) -1, -1, -1)]
	result = 0
	for i in digits:
		result += i
	if len(str(result)) >= 2:
		return digital_root(result)
	return result


print(digital_root(132189))