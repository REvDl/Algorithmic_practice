from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths_tree = []
        def dfs(node, path_tree):
            if not path_tree:
                path_tree += str(node.val)
            else:
                path_tree += f"->{node.val}"
            if node.left:
                dfs(node.left, path_tree)
            if node.right:
                dfs(node.right, path_tree)
            if not node.left and not node.right:
                paths_tree.append(path_tree)
                path_tree = ""
        dfs(root, "")
        return paths_tree
