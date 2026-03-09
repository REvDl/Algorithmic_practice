from typing import List


def stalin_sort_v1(arr: List[int]):
	stalin = arr[0]
	result = []
	for i in range(len(arr)):
		if arr[i] >= stalin:
			result.append(arr[i])
			stalin = arr[i]
	return result

def stalin_sort(arr):
	if not arr:
		return
	stalin = arr[0]
	i = 0
	while i < len(arr):
		if arr[i] >= stalin:
			stalin = arr[i]
			i += 1
		else:
			del arr[i]
	return arr




#[1, 2, 2, 3, 4]
arr = []
print(stalin_sort(arr))

"""
пока 0 < 3
если 5 >= 5 



"""