"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_t_map = {}
        t_s_map = {}
        
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s in s_t_map:
                if s_t_map[char_s] != char_t:
                    return False
            else:
                s_t_map[char_s] = char_t
            if char_t in t_s_map:
                if t_s_map[char_t] != char_s:
                    return False
            else:
                t_s_map[char_t] = char_s
        return True

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
