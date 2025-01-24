'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.
'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        total = 1
        sqrt_num = int(num**0.5)

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total == num
