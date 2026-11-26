


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hash_needle = 0
        hash_haystack = 0
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_haystack < len_needle:
            return -1
        b = 31
        mod = (1 << 61) - 1
        for char in needle:
            pos_letter = ord(char) - ord('a') + 1
            hash_needle = (hash_needle * b + pos_letter) % mod
        for i in range(len_needle):
            hash_haystack = (hash_haystack * b + (ord(haystack[i]) - ord('a') + 1)) % mod
        max_pow = pow(b, len_needle - 1, mod)
        if hash_haystack == hash_needle:
            return 0
        for right in range(len_needle, len_haystack):
            old_letter_pos = ord(haystack[right - len_needle]) - ord('a') + 1
            curr_letter_pos = ord(haystack[right]) - ord('a') + 1
            hash_haystack = ((hash_haystack - old_letter_pos * max_pow) * b + curr_letter_pos) % mod
            if hash_haystack == hash_needle:
                return right - len_needle + 1
        return -1



obj = Solution()
haystack = "aaa"
needle = "aaaa"
print(obj.strStr(haystack, needle))
