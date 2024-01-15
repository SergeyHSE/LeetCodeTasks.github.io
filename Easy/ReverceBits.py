"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = bin(n)[2:].zfill(32)
        reversed_str = binary_str[::-1]
        reversed_n = int(reversed_str, 2)
        return reversed_n
      
