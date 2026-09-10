

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


    def averageOfSubtree(self, root: TreeNode) -> int:
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
