'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:  # Leaf node
                if is_left:
                    return node.val
                else:
                    return 0
            left_sum = dfs(node.left, True)   # Traverse left child
            right_sum = dfs(node.right, False)  # Traverse right child
            return left_sum + right_sum
        
        return dfs(root, False)
