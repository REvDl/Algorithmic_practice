def YoutubeSorting(data:list[int]) -> list[int]:
	best_nazi = max(data)
	result = []
	for i in data:
		if i != best_nazi:
			continue
		result.append(i)
	return result




print(YoutubeSorting([10, 20, 10, 20, 10]))