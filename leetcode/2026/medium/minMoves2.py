


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(num - mid) for num in nums)






obj = Solution()
nums = [1, 2, 3]
print(obj.minMoves2(nums))
