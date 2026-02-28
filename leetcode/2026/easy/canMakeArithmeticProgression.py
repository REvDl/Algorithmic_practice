class Solution_v1:
	def canMakeArithmeticProgression_v1(self, arr: list[int]) -> bool:
		sort_arr = sorted(arr)
		difference = sort_arr[1] - sort_arr[0]
		for i in range(2, len(sort_arr)):
			if sort_arr[i] - sort_arr[i-1] != difference:
				return False
		return True


class Solution:
	def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
		arr.sort()
		difference = arr[1] - arr[0]
		for i in range(2, len(arr)):
			if arr[i] - arr[i - 1] != difference:
				return False
		return True

obj = Solution()
print(obj.canMakeArithmeticProgression([3,5,1]))