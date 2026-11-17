


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        best_num, best_idx = None, None
        for idx, num in enumerate(nums):
            if num < target:
                if best_num is None or num > best_num:
                    best_num = num
                    best_idx = idx
        if nums[0] > target:
            return 0
        return best_idx + 1

obj = Solution()
nums = [1,3,5,6]
target = 7
print(obj.searchInsert(nums, target))
