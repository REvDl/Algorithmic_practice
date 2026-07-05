from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        rows, cols = len(board), len(board[0])
        MOD = 10**9+7
        dp = [[[-1, 0] for _ in range(cols)] for _ in range(rows)]
        dp[rows-1][cols-1] = [0, 1]
        for i in range(rows -1, -1, -1):
            for j in range(cols -1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                char = board[i][j]
                if char == 'X':
                    continue
                num = 0 if char in ['E', 'S'] else int(char)
                max_sum = -1
                path = 0
                directions = [(i+1, j), (i, j+1), (i+1, j+1)]
                for nr, nc in directions:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        prev_sum, prev_path = dp[nr][nc]
                        if prev_sum > max_sum:
                            max_sum = prev_sum
                            path = prev_path
                        elif prev_sum == max_sum and max_sum != -1:
                            path = (path + prev_path) % MOD
                if max_sum != -1:
                    dp[i][j] = [max_sum + num, path]
        prev_sum, prev_path = dp[0][0]
        if prev_sum == -1:
            return [0, 0]
        return [prev_sum, prev_path]



obj = Solution()
board = ["E11","XXX","11S"]
print(obj.pathsWithMaxScore(board))












