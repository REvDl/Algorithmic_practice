

class Solution:
    def canSorting(self, nums: list[int]) -> tuple[bool, int, int] | bool:
        check_diff = None
        n = len(nums)
        if n <= 1:
            return True
        for i in range(1, len(nums) - 1):
            if nums[i-1] > nums[i]:
                if check_diff:
                    return False
                check_diff = True
            else:
                if check_diff is False:
                    return False
                check_diff = True
        if nums[-2] > nums[-1]:
            if check_diff:
                return False
        else:
            if check_diff is False:
                return False
        return True, min(nums), max(nums)


    def sortableIntegers(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        k = n
        while k > 0:
            prev_chunk = []
            for i in range(0, n, k):
                chunk = nums[i:i + k]
                if n % k == 0 and self.canSorting(chunk):
                    if prev_chunk:
                        if chunk[0] <= prev_chunk[-1]:
                            continue
                        else:
                            break
                    prev_chunk = chunk
            else:
                res += k
            k -= 1
        res += k
        return res




obj = Solution()
nums = [[7,6,5], [3,1,2], [5,8]]
for num in nums:
    print(obj.canSorting(num))
    print(obj.sortableIntegers(num))
