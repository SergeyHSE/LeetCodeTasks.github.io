"""
Given a roman numeral, convert it to an integer.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}        
        r = 0
        v_p = 0
        for i in s:
            v = r_d[i]
            if v > v_p:
                r += v - 2 * v_p
            else:
                r += v
            v_p = v
        return r

# Another solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}

        s = list(s)

        c = r_d[s[0]]
        r = r_d[s[0]]

        for i in s[1:]:
            if r_d[i] > r:
                c += r_d[i] - 2 * r
            else:
                c += r_d[i]
            r = r_d[i]
        return c
