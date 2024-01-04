"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        m = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for i in s:
            if i in m.values():
                st.append(i)
            elif i in m.keys():
                if not st or st.pop() != m[i]:
                    return False   
        return not st
