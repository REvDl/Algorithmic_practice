from collections import Counter, deque

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        sorted_chars = sorted(s)
        count_chars = Counter(sorted_chars)
        pair_chars = deque()
        one_chars = []
        for char in sorted_chars[::-1]:
            if count_chars[char] >= 2:
                pair_chars.append(char)
                pair_chars.appendleft(char)
                count_chars[char] -= 2
            elif count_chars[char] == 1:
                one_chars.append(char)
                count_chars[char] -= 1
            else:
                continue
        mid = len(pair_chars) // 2
        pair_chars = list(pair_chars)
        return "".join(pair_chars[:mid]) + "".join(one_chars) + "".join(pair_chars[mid:])





obj = Solution()
s = "yey"
print(obj.smallestPalindrome(s))
