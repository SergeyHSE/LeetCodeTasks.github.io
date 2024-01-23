"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        memo = {}

        def Mirror(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False

            if (left, right) in memo:
                return memo[(left, right)]

            result = Mirror(left.left, right.right) and Mirror(left.right, right.left)
            memo[(left, right)] = result

            return result

        return not root or Mirror(root.left, root.right)
        



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def Mirror(root_left, root_right):
            if not root_left and not root_right:
                return True
            elif not root_left and root_right:
                return False
            elif root_left and not root_right:
                return False
            elif root_left.val != root_right.val:
                return False
            left = Mirror(root_left.left, root_right.right)
            right = Mirror(root_left.right, root_right.left)
            return left and right
            
        return Mirror(root.left, root.right)
