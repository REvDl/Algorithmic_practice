


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        length_array = []
        length = 1
        for i in range(1, len(t)):
            if t[i-1] == t[i]:
                length += 1
            else:
                length_array.append((t[i-1], length))
                length = 1
        max_gain = 0
        for i in range(1, len(length_array) - 1):
            prev_char, prev_length = length_array[i-1]
            curr_char, curr_lenght = length_array[i]
            next_char, next_length = length_array[i+1]
            if curr_char == '1' and prev_char == '0' and next_char == '0':
                max_gain = max(max_gain, prev_length + next_length)
        return s.count('1') + max_gain



obj = Solution()
s = "1000100"
print(obj.maxActiveSectionsAfterTrade(s))



