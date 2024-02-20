"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i // 2] + (i % 2)
        return result
