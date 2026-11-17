


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid - 1
        return left



obj = Solution()
nums = [1,3,5,6]
target = 7
print(obj.searchInsert(nums, target))
