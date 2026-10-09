

class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        added = 0
        can_closed = False
        for char in s:
            if char == "(":
                if can_closed:
                    if count > 0:
                        added += 1
                        count -= 1
                    else:
                        added += 2
                    can_closed = False
                count += 1
            else:
                if count > 0:
                    if can_closed:
                        count -= 1
                        can_closed = False
                    else:
                        can_closed = True
                elif count <= 0:
                    if can_closed:
                        added += 1
                        can_closed = False
                    else:
                        can_closed = True
        if can_closed:
            if count > 0:
                added += 1
                count -= 1
            else:
                added += 2
        return added + count * 2




obj = Solution()
s = ["(()))","())","))())("]
for char in s:
    print(obj.minInsertions(char))
