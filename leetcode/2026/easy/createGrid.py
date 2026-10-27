


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ['.' + '#' * (n - 1) for _ in range(m - 1)]
        return grid + ['.' * n]

obj = Solution()
m = 10
n = 15
print(obj.createGrid(m, n))
