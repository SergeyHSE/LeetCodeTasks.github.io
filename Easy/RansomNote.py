"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # Count letter occurrences in magazine
        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Check if ransomNote can be formed from magazine
        for char in ransomNote:
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1
        
        return True
      
