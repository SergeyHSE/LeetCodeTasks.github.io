'''
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_rows = 0
        x = n

        while x >= 0:
            number_rows += 1
            x = x - number_rows
        return number_rows - 1
