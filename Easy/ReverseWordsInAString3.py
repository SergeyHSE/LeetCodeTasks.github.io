'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        result = []

        for i in range(len(s)):
            x = s[i][::-1]
            result.append(x)
        
        return ' '.join(result)
