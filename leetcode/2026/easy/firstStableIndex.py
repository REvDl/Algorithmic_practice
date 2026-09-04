

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = float("inf")
        for i in range(n):
            stable_index = max(nums[0:i+1], default=nums[0]) - min(nums[i:n], default=0)
            if stable_index <= k:
                res = min(i, res)
        return res if res != float("inf") else -1




obj = Solution()
nums = [0]
k = 0
print(obj.firstStableIndex(nums, k))
