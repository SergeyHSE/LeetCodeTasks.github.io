"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        count_nums1 = {}
        count_nums2 = {}

        for num in nums1:
            count_nums1[num] = count_nums1.get(num, 0) + 1
        for num in nums2:
            count_nums2[num] = count_nums2.get(num, 0) + 1
        result = []
        for num in set(nums1) & set(nums2):
            result.extend([num] * min(count_nums1[num], count_nums2[num]))
        return result
