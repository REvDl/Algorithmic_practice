


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        res = 0
        even, odd = 1, 0
        curr_sum = 0
        for right in range(1, n + 1):
            num = arr[right - 1]
            curr_sum += num
            if curr_sum % 2 == 0:
                even += 1
                res += odd
            else:
                odd += 1
                res += even
        return res % (10 ** 9 + 7)



obj = Solution()
arr = [[1,3,5], [2,4,6]]
for nums in arr:
    print(obj.numOfSubarrays(nums))
