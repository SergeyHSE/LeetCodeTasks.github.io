'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
'''

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        result = []
        if word.isupper() == True:
            return True
        
        if word.islower() == True:
            return True

        if word.islower() == False and word.isupper() == False:
            if word[0].isupper() == True:
                result.append(word[0])
            else:
                return False

            for i in range(1, len(word)):
            
                if word[i].islower() == True:
                    result.append(word[i])

            return len(result) == len(word)
