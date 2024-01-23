"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, result):
            if not node:
                return
            path += str(node.val)
            
            if not node.left and not node.right:
                result.append(path)
                return
            path += '->'
            
            dfs(node.left, path, result)
            dfs(node.right, path, result)
            
        result = []
        dfs(root, '', result)
        return result
