

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        left = 0
        count = 0
        for right in range(len(nums)):
            num = nums[right]
            if not (num >= minK and num <= maxK):
                left = right + 1
                continue
            count += right - left + 1
        return count


obj = Solution()
nums = [1,4,7,2]
minK = 1
maxK = 5
print(obj.countSubarrays(nums, minK, maxK))
