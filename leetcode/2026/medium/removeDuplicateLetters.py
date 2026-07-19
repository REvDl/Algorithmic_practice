class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count_char = Counter(s)
        visited = set()
        for char in s:
            count_char[char] -= 1
            if char in visited:
                continue
            visited.add(char)
            while stack and stack[-1] > char and count_char[stack[-1]] > 0:
                visited.remove(stack[-1])
                stack.pop()
            stack.append(char)
        return "".join(stack)
