


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        res = 0
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        for left in range(n + 1):
            for k in range(n + 1):
                if (left + k) <= n:
                    curr_sum = prefix_sum[left + k] - prefix_sum[left]
                    if curr_sum % 2 != 0:
                        res += 1
        return res % (10 ** 9 + 7)


obj = Solution()
arr = [[1,3,5], [2,4,6]]
for nums in arr:
    print(obj.numOfSubarrays(nums))
