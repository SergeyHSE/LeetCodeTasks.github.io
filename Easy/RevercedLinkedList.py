"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
