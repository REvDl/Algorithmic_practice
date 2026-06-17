class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        curr_len = 0
        for i in range(n):
            char = s[i]
            if char.islower():
                curr_len += 1
            elif char == '*':
                curr_len = max(0, curr_len - 1)
            elif char == '#':
                curr_len *= 2
            lengths[i] = curr_len
        if k >= lengths[-1]:
            return '.'
        for i in range(n - 1, -1, -1):
            char = s[i]
            curr_len = lengths[i]
            prev_len = lengths[i - 1] if i > 0 else 0
            
            if char == '#':
                if k >= prev_len:
                    k %= prev_len
            elif char == '%':
                k = curr_len - 1 - k
            elif char.islower():
                if k == curr_len - 1:
                    return char
                    
        return '.'
