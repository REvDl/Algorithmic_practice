

class Solution:
    def canSorting(self, nums: list[int], start: int, end: int) -> tuple[bool, int, int]:
        end = min(end, len(nums)) 
        if end - start <= 1:
            num = nums[start] if start < len(nums) else 0
            return True, num, num 
        count = 0
        max_num = nums[start]
        min_num = nums[start]
        if nums[end - 1] > nums[start]:
            count += 1
        for i in range(start, end - 1):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[i])
            if nums[i] > nums[i + 1]:
                count += 1
            if count > 1:
                return False, 0, 0
        max_num = max(max_num, nums[end - 1])
        min_num = min(min_num, nums[end - 1])
        return count <= 1, min_num, max_num

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        k = n
        while k >= 1:
            if n % k != 0:
                k -= 1
                continue
            prev_end = float('-inf')
            can_sort = False
            for i in range(0, n, k):
                result = self.canSorting(nums, i, i+k)
                if result[0]:
                    if result[1] >= prev_end:
                        prev_end = result[2]
                        can_sort = True
                    else:
                        can_sort = False
                        break
                else:
                    can_sort = False
                    break
            if can_sort:
                res += k
            k -= 1
        return res





obj = Solution()
nums = [[7,6,5], [3,1,2], [5,8]]
for num in nums:
    print(obj.sortableIntegers(num))
