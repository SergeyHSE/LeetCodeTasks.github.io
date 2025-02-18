'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def lenth(node, result):
            if not node:
                return 0
            left = lenth(node.left, result)
            right = lenth(node.right, result)

            result[0] = max(result[0], left + right)

            return max(left, right) + 1

        result = [0]
        lenth(root, result)

        return result[0]
