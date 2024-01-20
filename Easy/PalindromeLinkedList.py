"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
 """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values == values[::-1]
