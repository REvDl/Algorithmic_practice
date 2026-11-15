


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        res = 0
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        even_odd = [(0, 0)] * (n + 1)
        for i in range(1, n + 1):
            prev_even, prev_odd = even_odd[i - 1]
            if prefix_sum[i - 1] % 2 == 0:
                prev_even += 1
            else:
                prev_odd += 1
            even_odd[i] = (prev_even, prev_odd)
        for right in range(1, n + 1):
            even, odd = even_odd[right]
            if prefix_sum[right] % 2 == 0:
                res += odd 
            else:
                res += even
        return res % (10 ** 9 + 7)


obj = Solution()
arr = [[1,3,5], [2,4,6]]
for nums in arr:
    print(obj.numOfSubarrays(nums))
