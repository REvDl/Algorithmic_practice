import string



class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = ""
        curr_str = ""
        for char in s:
            if char in string.ascii_lowercase:
                curr_str += char
            elif char == "[":
                stack.append((curr_str, curr_num))
                curr_num = ""
                curr_str = ""
            elif char == "]":
                prev_str, prev_num = stack.pop()
                prev_str += curr_str * int(prev_num)
                curr_str = prev_str
            else:
                curr_num += char
        return curr_str

obj = Solution()
s = ["3[a2[c]]", "2[abc]3[cd]ef"]
for t in s:
    print(obj.decodeString(t))
