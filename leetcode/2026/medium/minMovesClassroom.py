from typing import List
from collections import deque




class Solution:
    def _bfs(self, rows:int, cols:int, matrix, x:int, y:int, energy:int, let:int, total_let:int, l_garbage_ids):
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = {(x, y, energy, let)}
        q = deque([(x, y, energy, let, 0)]) 
        max_e = energy
        while q:
            r, c, energy, let, steps = q.popleft()
            if let == (1 << total_let) - 1:
                return steps
            elif energy == 0 and matrix[r][c] != "R":
                continue
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != "X":
                    if matrix[nr][nc] == "R":
                        if (nr, nc, max_e, let) not in visited:
                            visited.add((nr, nc, max_e, let))
                            q.append((nr, nc, max_e, let, steps+1))
                        continue
                        
                    elif matrix[nr][nc] == "L":
                        garbage_id = l_garbage_ids[(nr, nc)]
                        new_mask = let | (1 << garbage_id)
                        if (nr, nc, energy-1, new_mask) not in visited:
                            visited.add((nr, nc, energy-1, new_mask))
                            q.append((nr, nc, energy-1, new_mask, steps+1))
                        continue
                        
                    else:
                        if (nr, nc, energy-1, let) not in visited:
                            visited.add((nr, nc, energy-1, let))
                            q.append((nr, nc, energy-1, let, steps+1))
                        continue

        return -1
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
        l_garbage_ids = {} 
        l_counter = 0
        total_let = 0
        S = None
        for r in range(rows):
            for c in range(cols):
                cell = matrix[r][c]
                if cell == "L":
                    l_garbage_ids[(r, c)] = l_counter
                    l_counter += 1
                elif cell == "S":
                    S = (r, c)
        total_let = l_counter
        initial_mask  = 0
        return self._bfs(rows, cols, matrix, S[0], S[1], energy, initial_mask, total_let, l_garbage_ids)



obj = Solution()
classroom = ["L.", "R.", "LL", "S.", "L.", "XR", ".."]
energy = 7
print(obj.minMoves(classroom, energy))
