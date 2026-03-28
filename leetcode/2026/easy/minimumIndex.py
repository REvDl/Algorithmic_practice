class Solution:
	def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
		result_index = {}
		for num in range(len(capacity)):
			if capacity[num] >= itemSize:
				if capacity[num] not in result_index:
					result_index[capacity[num]] = num
		return result_index[min(result_index)] if len(result_index) > 0 else -1


obj = Solution()
arr = [7,7]
print(obj.minimumIndex(arr, 3))