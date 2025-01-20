'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        unique_nums = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in unique_nums:
                result.append(i)

        return result
