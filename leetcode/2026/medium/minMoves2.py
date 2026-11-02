


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res = 0
        mid = nums[len(nums) // 2]
        for num in nums:
            if num > mid:
                res += num - mid
            elif num < mid:
                res += mid - num
        return res






obj = Solution()
nums = [1, 2, 3]
print(obj.minMoves2(nums))
