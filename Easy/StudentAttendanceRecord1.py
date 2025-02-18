'''
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0

        for i in range(len(s)):
            if s[i] == 'A':
                count_A += 1
                if count_A >= 2:
                    return False
            if i >= 2 and s[i] == s[i-1] == s[i-2] == 'L':
                return False
        return  count_A < 2    
