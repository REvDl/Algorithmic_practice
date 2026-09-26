

class Solution:
    def removeElement(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k == 0:
            return True
        for num in nums:
            new_sum = total_sum - (2 * num)
            if new_sum % k == 0:
                return True
        return False


    def is_valid(self, total_sum: int, k: int) -> bool:
        if total_sum % k == 0:
            return True
        return False

    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_length = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if self.removeElement(nums[i:j], k):
                    max_length = max(max_length, j - i)
        return max_length 


obj = Solution()
nums = [5,3,4]
k = 7
print(obj.longestSubarray(nums, k))
