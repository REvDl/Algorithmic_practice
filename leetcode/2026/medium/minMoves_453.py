


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_n = min(nums)
        return sum([num - min_n for num in nums])


obj = Solution()
nums = [[1,2,3], [-10, -5, -1]]
for num in nums:
    print(obj.minMoves(num))
