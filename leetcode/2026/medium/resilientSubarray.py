

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        max_len = 0
        curr_len = 0
        n = len(nums)
        for i in range(n):
            r = nums[i] % k
            if i == 0 or r == (nums[i-1] % k):
                curr_len += 1
                if (curr_len - 1) * r % k == 0:
                    max_len = max(max_len, curr_len)
            else:
                if (curr_len - 1) * (nums[i-1] % k) % k == 0:
                    max_len = max(max_len, curr_len)
                curr_len = 1
        if (curr_len - 1) * (nums[-1] % k) % k == 0:
            max_len = max(max_len, curr_len)
        else:
            max_len = max(max_len, 1) 
        return max_len




obj = Solution()
nums = [2,4,6,3]
k = 2
print(obj.resilientSubarray(nums, k))
