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

# Anpther solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix
