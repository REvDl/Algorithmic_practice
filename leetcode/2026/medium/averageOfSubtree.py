

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _averageForNode(self, root: TreeNode) -> float:
        stack = [root]
        count = 1 if root else 0
        res = 0
        while stack:
            curr = stack.pop()
            if curr:
                if curr.left:
                    count += 1
                    stack.append(curr.left)
                if curr.right:
                    count += 1
                    stack.append(curr.right)
                res += curr.val
        return res // count


    def averageOfSubtree_v1(self, root: TreeNode) -> int:
        stack = [root]
        res = 0
        while stack:
            curr = stack.pop()
            if curr:
                res += 1 if self._averageForNode(curr) == curr.val else 0
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return res

    
    def averageOfSubtree_v2(self, root: TreeNode) -> int:
        count = 0
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0,0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                nonlocal count
                count += 1
            return total_sum, total_count
        dfs(root)
        return count


    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0,0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                dfs.count += 1
            return total_sum, total_count
        dfs.count = 0
        dfs(root)
        return dfs.count



