import math



class Solution:
    def generate_permutations(self, nums: list[int]):
        if not nums:
            return []
        result = []
        def permute(arr, start):
            if start == len(arr) - 1:
                result.append(list(arr))
                return
            for i in range(start, len(arr)):
                current = list(arr)
                current[start], current[i] = current[i], current[start]
                permute(current, start + 1)
        permute(nums, start=1)
        return result



    def numOfWays(self, nums: list[int]) -> int:
        root = nums[0]
        n = len(nums)
        def max_min_positions(nums: list[int]):
            max_nums, min_nums = [], []
            for i in range(1, n):
                num = nums[i]
                if num > root:
                    max_nums.append(num)
                else:
                    min_nums.append(num)
            return max_nums, min_nums
        valid_tree = max_min_positions(nums)
        combinations = self.generate_permutations(nums)
        res = 0
        for combination in combinations:
            for_check = max_min_positions(combination)
            if for_check == valid_tree:
                res += 1

        return res % (10 ** 9 + 7) - 1
        #x, y = len(min_nums), len(max_nums)
        #combination =(math.factorial(x + y)) // (math.factorial(x) * math.factorial(y))
        #return combination % MOD - 1




obj = Solution()
nums = [[2, 1, 3], [2, 3, 1], [1,2,3], [3,4,5,1,2]]
print(obj.generate_permutations(nums[0]))
for num in nums:
    print(obj.numOfWays(num))
