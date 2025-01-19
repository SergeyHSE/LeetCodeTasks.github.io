'''
Given a 32-bit integer num, return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.
'''

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        hex_map = '0123456789abcdef'
        result = ""

        for _ in range(8):  # Maximum 8 hexadecimal digits for 32-bit integer
            result = hex_map[num & 0xf] + result  # Get the last 4 bits and append to result
            num >>= 4  # Shift num right by 4 bits

        # Remove leading zeros
        while result[0] == '0':
            result = result[1:]

        return result
