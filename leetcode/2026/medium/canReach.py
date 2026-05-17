from typing import List







class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr) - 1
        visited = set()
        def dfs(index_node, visited):
            if 0 > index_node or index_node > n or index_node in visited:
                return False
            elif arr[index_node] == 0:
                return True 
            elif index_node not in visited:
                visited.add(index_node)
                right_node = index_node + arr[index_node]
                left_node = index_node - arr[index_node]
                for i in (right_node, left_node):
                    if dfs(i, visited):
                        return True
                return False
        return dfs(start, visited)




obj = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(obj.canReach(arr, start))
