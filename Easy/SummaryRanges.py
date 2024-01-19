"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        n = len(nums)

        i = 0
        while i < n:
            begin = nums[i]
            while i < n - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]
            result.append("{}->{}".format(begin, end) if begin != end else str(begin))
            i += 1

        return result
