"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            set_nums.add(num)
        return False

# Another, but Q(n^2) complexity

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

# Another, Q(n) complexity

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
