"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s_x = str(x)
        return s_x == s_x[::-1]
      
