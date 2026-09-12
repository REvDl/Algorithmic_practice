from collections import Counter



class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = Counter(nums)
        visited = set()
        res = 0
        for num in nums:
            if count[num] >= 3 and num not in visited:
                visited.add(num)
                indices = [i for i, v in enumerate(nums) if v == num]
                if indices[1] - indices[0] == indices[2] - indices[1]:
                    res += 1
            else:
                continue
        return res


obj = Solution()
nums = [1,2,1,2,1,2,3,4,3,4,3,4]
print(obj.countSpecialIntegers(nums))
