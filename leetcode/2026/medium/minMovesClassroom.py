from typing import List
from collections import deque




class Solution:
    def _bfs(self, rows:int, cols:int, matrix, x:int, y:int, energy:int, let:int, total_let:int, steps:int):
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = {(x,y)}
        q = deque([(x,y)])
        max_e = energy
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and matrix[nr][nc] != "X":
                    steps += 1
                    energy -= 1
                    if energy == 0 and matrix[nr][nc] != "R":
                        print("break")
                        break
                    elif matrix[nr][nc] == "L":
                        let += 1
                    elif matrix[nr][nc] == "R":
                        print("RR")
                        energy = max_e
                    visited.add((nr, nc))
                    q.append((nr, nc))
        return steps
    def minMoves(self, classroom: List[str], energy: int) -> int:
        """
        S - start position
        L - garbage for collection
        R - charge energy
        X - let
        . - empty position
        """
        n = len(classroom)
        matrix = [list(row) for row in classroom]
        rows, cols = len(matrix), len(matrix[0])
        total_let = 0
        S = None
        for i, row in enumerate(matrix):
            total_let += row.count("L")
            if not S and "S" in row:
                j = row.index("S")
                S = (i, j)
                continue
        return self._bfs(rows, cols, matrix, S[0], S[1], energy, 0, total_let, 0)




obj = Solution()
classroom =["S.", "XL"]
energy = 2
print(obj.minMoves(classroom, energy))
