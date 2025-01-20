'''
Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        split_txt = s.split()
        count = 0
        for i in range(len(split_txt)):
            count += 1
        return count
