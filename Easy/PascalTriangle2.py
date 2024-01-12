"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]
        return result
