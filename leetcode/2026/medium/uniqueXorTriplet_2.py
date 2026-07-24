from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        unique_xor_pair = set()
        for i in range(n):
            for j in range(i, n):
                unique_xor_pair.add(nums[i] ^ nums[j])
        ans = 0
        result_xor = set()
        for xor in unique_xor_pair:
            for num in nums:
                result_xor.add(xor ^ num) 
        return len(result_xor)


obj = Solution()
nums = [8,7,8,10]
print(obj.uniqueXorTriplets(nums))
