'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        stack = []
        current = root
        prev_val = None
        current_count = 0
        max_count = 0
        modes = []

        # Iterative in-order traversal
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()

            # Handle the current node's value
            if current.val != prev_val:
                prev_val = current.val
                current_count = 0
            current_count += 1

            # Update modes
            if current_count > max_count:
                max_count = current_count
                modes = [current.val]
            elif current_count == max_count:
                modes.append(current.val)

            # Move to the right subtree
            current = current.right

        return modes
