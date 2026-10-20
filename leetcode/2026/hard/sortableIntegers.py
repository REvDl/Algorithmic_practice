

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        k = n
        while k > 0:
            if n % k != 0:
                k -= 1
                continue
            count = 0
            for i in range(n):
                start_block = (i // k) * k
                j = 0
                if i == k - 1:
                    j = (i + 1) % k
                next_idx = start_block + j
                if nums[i] > nums[next_idx]:
                    count += 1
                if count > 1:
                    break
            res += k
            k -= 1
        return res


#                    start_block = (i // k) * k
#                    j = (i + 1) % k





obj = Solution()
nums = [[7,6,5], [3,1,2], [5,8]]
for num in nums:
    print(obj.sortableIntegers(num))
