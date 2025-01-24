'''
Given an integer num, return a string of its base 7 representation.
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        negative = num < 0
        num = abs(num)
        base7 = []

        while num > 0:
            base7.append(str(num % 7))
            num //= 7
        
        result = ''.join(base7[::-1])

        if negative is True:
            return '-' + result
        else:
            return result
