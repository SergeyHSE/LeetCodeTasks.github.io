"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = int(a, 2)
        num_b = int(b, 2)
        result = num_a + num_b
        return bin(result)[2:]
      
