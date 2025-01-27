'''
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on.
The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
'''

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_score = sorted(score, reverse=True)
        dict_result = {}

        
        for i, j in enumerate(sorted_score, start=1):
            if i == 1:
                dict_result[j] = 'Gold Medal'
            elif i == 2:
                dict_result[j] = 'Silver Medal'
            elif i == 3:
                dict_result[j] = 'Bronze Medal'
            else:
                dict_result[j] = str(i)
        return [dict_result[j] for j in score] 
