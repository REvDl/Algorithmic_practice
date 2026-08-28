from collections import Counter



class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        n = len(s)
        chars = [char for char, qua in count.items() if qua % 2 != 0]
        if len(chars) > 1:
            return ""
        mid_char = chars[0] if chars else ""
        half_count = Counter()
        for char, qua in count.items():
            half_count[char] = qua // 2
        greater_string = []
        half_n = n // 2
        for i in range(half_n):
            char = target[i]
            if half_count[char] > 0:
                greater_string.append(char)
                half_count[char] -= 1

                res = "".join(half_count.elements())
                left_suffix_target = "".join(sorted(res, reverse=True))
                right_suffix_target = "".join(sorted(res))

                current_prefix = "".join(greater_string)
                potential_palindrome = current_prefix + left_suffix_target + mid_char + right_suffix_target + current_prefix[::-1]
                if potential_palindrome > target:
                    continue

                greater_string.pop()
                half_count[char] += 1
            available_chars = sorted(half_count.keys())
            for sorted_char in available_chars:
                if sorted_char > char and half_count[sorted_char] > 0:
                    greater_string.append(sorted_char)
                    half_count[sorted_char] -= 1

                    remaining = "".join(sorted(half_count.elements()))
                    left_half = "".join(greater_string) + remaining
                    return left_half + mid_char + left_half[::-1]
            return ""
        left_half = "".join(greater_string)
        palindrome = left_half + mid_char + left_half[::-1]
        return palindrome if palindrome > target else ""



obj = Solution()
s = "baba"
target = "abba"
print(obj.lexPalindromicPermutation(s,target))
