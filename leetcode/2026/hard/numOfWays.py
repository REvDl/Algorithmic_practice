import math



class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        root = nums[0]
        n = len(nums)
        max_nums, min_nums = [], []
        for i in range(1, n):
            num = nums[i]
            if num > root:
                max_nums.append(num)
            else:
                min_nums.append(num)
        x, y = len(min_nums), len(max_nums)
        combination =(math.factorial(x + y)) // (math.factorial(x) * math.factorial(y))
        return combination % MOD - 1




obj = Solution()
nums = [[3,4,5,1,2], [2,1,3]]
for num in nums:
    print(obj.numOfWays(num))
