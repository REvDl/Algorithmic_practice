# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right




root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)


class Solution(object):
    def sumRootToLeaf(self, root):
        def is_node(node, current_sum):
            if not node:
                return 0
            current_sum = (current_sum << 1) + node.val
            if not node.left and not node.right:
                return current_sum
            return is_node(node.left, current_sum) + is_node(node.right, current_sum)
        return is_node(root, 0)

obj = Solution()
print(obj.sumRootToLeaf(root))
