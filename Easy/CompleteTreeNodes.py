"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            # Left subtree is a perfect binary tree
            return 2 ** left_height + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree
            return 2 ** right_height + self.countNodes(root.left)

    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

# Another easy solution
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        return self.countNodes(root.left) + self. countNodes(root.right) + 1
