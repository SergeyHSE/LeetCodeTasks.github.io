"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = None
        count = 0
        for i in nums:
            if count == 0:
                x = i
            count += (1 if i == x else -1)
        return x

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        majority_element = max(count, key=count.get)
        return majority_element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1
        majority_count = len(nums) // 2
        for num, count in counts.items():
            if count > majority_count:
                return num
