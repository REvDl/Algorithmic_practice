


class Solution:
    def canAliceWin(self, n: int) -> bool:
        steps = 0
        for i in range(10, 0, -1):
            if n < i:
                break
            n -= i
            steps += 1
        return steps % 2 != 0


obj = Solution()
nums = [12, 1, 39, 11, 34, 50]
for num in nums:
    print(obj.canAliceWin(num))
