'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = list(s)

        for i in range(0, len(s), k*2):
            result[i:i+k] = reversed(result[i:i+k])
        
        return ''.join(result)
