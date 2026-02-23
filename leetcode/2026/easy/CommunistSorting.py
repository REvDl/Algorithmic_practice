

def communist(arr:list[int]):
	if not arr:
		return arr
	total = sum(arr)
	communist_value = total // len(arr)
	for i in range(len(arr)):
		arr[i] = communist_value
	return arr

arr = [10, 1, 1, 1, 2, 6, 10]
print(communist(arr))