"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number_set = set()
             
        while n != 1 and n not in number_set:
            number_set.add(n)
            n = str(n)
            num = 0
            for i in n:
                num += (int(i) ** 2)
            n = num
        return n == 1
