"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize an array to store the tribonacci numbers
        tribonacci_nums = [0] * (n + 1)
        tribonacci_nums[1] = 1
        tribonacci_nums[2] = 1

        # Calculate tribonacci numbers using dynamic programming
        for i in range(3, n + 1):
            tribonacci_nums[i] = tribonacci_nums[i - 1] + tribonacci_nums[i - 2] + tribonacci_nums[i - 3]

        return tribonacci_nums[n]        
