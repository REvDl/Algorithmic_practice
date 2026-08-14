from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        count_char = defaultdict(int)
        max_lenght = 0
        for right in range(n):
            char = s[right]
            count_char[char] += 1
            while count_char[char] > 2:
                count_char[s[left]] -= 1
                left += 1
            max_lenght = max(max_lenght, right - left + 1)
        return max_lenght



obj = Solution()
s = "aaaa"
print(obj.maximumLengthSubstring(s))
