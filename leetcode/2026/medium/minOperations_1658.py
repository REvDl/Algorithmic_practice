

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        ans = 0
        n = len(nums)
        left, right = 0, n - 1
        while True:
            if left > right:
                break
            num_left = nums[left]
            num_right = nums[right]
            ans += 1
            if num_left >= num_right and x - num_left >= 0:
                x -= num_left
                left += 1
            elif num_right > num_left and x - num_right >= 0:
                x -= num_right
                right -= 1
            elif x - num_left >= 0:
                x -= num_left
                left += 1
            elif x - num_right >= 0:
                x -= num_right
                right -= 1
            else:
                ans -= 1
                break
        return ans if x == 0 else -1

obj = Solution()
nums = [1,1,4,2,3]
x = 5
print(obj.minOperations(nums, x))
