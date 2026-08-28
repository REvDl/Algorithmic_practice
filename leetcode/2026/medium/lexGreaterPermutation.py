from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        greater_sring = []
        n = len(s)
        for i in range(n):
            char = target[i]
            if count[char] > 0:
                greater_sring.append(char)
                count[char] -= 1
                res = "".join(count.elements())
                sorted_target = "".join(sorted(res, reverse=True))
                if sorted_target > target[i+1:] and i <= n:
                    continue
                greater_sring.pop()
                count[char] += 1 
            available_chars = sorted(count.keys())
            for sorted_char in available_chars:
                if sorted_char > char and count[sorted_char] > 0:
                    greater_sring.append(sorted_char)
                    count[sorted_char] -= 1
                    remaining = "".join(sorted(count.elements()))
                    return "".join(greater_sring) + remaining
            return ""
        return ""
                




obj = Solution()
s = "abc"
target = "bba"
print(obj.lexGreaterPermutation(s, target))
