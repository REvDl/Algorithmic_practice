from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")
        for i in range(n):
            if word[i] == "":
                if current > ord("z"):
                    return ""
                char = chr(current)
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = char
                current += 1

        res = "".join(word)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] != lcp[i][j]:
                    return ""
        return res





obj = Solution()
arr = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
print(obj.findTheString(arr))
