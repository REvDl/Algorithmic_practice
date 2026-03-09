from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums:
			return 0
		i = 0
		for j in range(1, len(nums)):
			# nums[j] = 1, nums[I] = 1, на первом шаге, на втором уже будет nums[j] = 2, nums[i] по прежнему 1
			# то есть теперь nums[j] является уникальным, по тз его нужно подвинуть впред, т.е nums[i] = nums[j], а i мы сдвигаем вправо
			if nums[j] != nums[i]:
				nums[i] = nums[j]
				i += 1
		return i + 1

obj = Solution()
num_list = [
    [1, 1, 1, 1, 1],
    [1],
    [],
    [1, 1, 2, 3, 3],
    [-10, -10, -5, 0, 0, 3, 10, 10]
]

for index, nums in enumerate(num_list):
    # Копируем массив, так как removeDuplicates меняет его in-place
    test_arr = nums.copy()
    k = obj.removeDuplicates(test_arr)
    print(f"{index}: k = {k}, result = {test_arr[:k]}")