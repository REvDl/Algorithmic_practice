

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        curr_num = ""
        sign = "+"
        for idx, char in enumerate(s):
            if char.isdigit():
                curr_num += char
            if char in "+-*/" or idx == len(s) - 1:
                if sign == "+":
                    stack.append(int(curr_num))
                elif sign == "-":
                    stack.append(-int(curr_num))
                elif sign == "*":
                    last_num = stack.pop()
                    res = last_num * int(curr_num)
                    stack.append(res)
                elif sign == "/":
                    last_num = stack.pop()
                    res = int(last_num / int(curr_num))
                    stack.append(res)



                sign = char
                curr_num = ""
        return sum(stack)




obj = Solution()
#tests = ["3+2","3+2*2", " 3/2 ", " 3+5 / 2 "]
#for s in tests:
 #   print(obj.calculate(s))
s = "3+2"
print(obj.calculate(s))

