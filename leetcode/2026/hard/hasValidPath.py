from collections import deque


class Solution:
    def _checkBrace(self, braces: str) -> bool:
        stack = []
        valid = {
            ")":"(",
            }
        for char in braces:
            if char in valid.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != valid[char]:
                    return False
                stack.pop()
        return len(stack) == 0

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c, current_str):
            if r == rows - 1 and c == cols - 1:
                return self._checkBrace(current_str)

            if r + 1 < rows:
                if dfs(r + 1, c, current_str + grid[r + 1][c]):
                    return True
            if c + 1 < cols:
                if dfs(r, c + 1, current_str + grid[r][c + 1]):
                    return True
            return False
        return dfs(0, 0, grid[0][0])




obj = Solution()
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
print(obj.hasValidPath(grid))
