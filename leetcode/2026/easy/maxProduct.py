import heapq


class Solution:
    def maxProduct_v1(self, n: int) -> int:
        nums = [int(x) for x in str(n)]
        two_max = heapq.nlargest(2, nums)
        return two_max[0] * two_max[1]

    def maxProduct(self, n: int) -> int:
        nums = sorted(str(n))
        return int(nums[-1]) * int(nums[-2])


obj = Solution()
n = 124
res = obj.maxProduct(n)
print(res)
assert res == 8
