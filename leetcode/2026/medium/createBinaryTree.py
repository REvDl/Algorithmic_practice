from typing import List



 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right




class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node = {}
        child_val = set()
        for desc in descriptions:
            parent, child, isleft = desc[0], desc[1], desc[2]
            if parent not in node:
                node[parent] = TreeNode(parent)
            if child not in node:
                node[child] = TreeNode(child)
            child_val.add(child)
            if isleft == 0:
                node[parent].right = node[child]
            else:
                node[parent].left = node[child]
        for val in node:
            if val not in child_val:
                return node[val]
        
