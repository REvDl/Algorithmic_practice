import math



class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def combinations(nums1, nums2):
            x, y = len(nums1), len(nums2)
            return  math.factorial(x + y) // (math.factorial(x) * math.factorial(y))
        
        def bts(nums: list[int]):
            if len(nums) <= 1:
                return 1
            root = nums[0]
            max_nums, min_nums = [], []
            n = len(nums)
            for i in range(1, n):
                num = nums[i]
                if num > root:
                    max_nums.append(num)
                else:
                    min_nums.append(num)
            return (combinations(max_nums, min_nums) % (10 ** 9 + 7) * bts(min_nums) * bts(max_nums)) % (10 ** 9 + 7)
        return bts(nums) % (10 ** 9 + 7) - 1

obj = Solution()
nums = [[3,4,5,1,2], [2,1,3]]
for num in nums:
    print(obj.numOfWays(num))
