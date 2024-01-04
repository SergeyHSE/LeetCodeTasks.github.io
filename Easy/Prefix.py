"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, s):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not s: 
            return ""

        f_s = min(s, key=len) 
        for i in range(len(f_s)):
            for j in s:
                if f_s[i] != j[i]:
                    return f_s[:i]

        return f_s 
