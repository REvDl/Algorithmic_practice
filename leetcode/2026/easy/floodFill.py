from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        comparison_color = image[sr][sc]
        if comparison_color == color:
            return image
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == comparison_color:
                        image[nr][nc] = color
                        queue.append((nr, nc))
            return image
        return bfs(sr, sc)

obj = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(obj.floodFill(image, sr, sc, color))

