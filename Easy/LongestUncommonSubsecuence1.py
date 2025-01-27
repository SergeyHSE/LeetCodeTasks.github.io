'''
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.
An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) != len(b):
            return max(len(a), len(b))

        for i in range(max(len(a), len(b))):

            if a[i] != b[i]: 
                return max(len(a), len(b))
        
        return -1 
