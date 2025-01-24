'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'
        result = []
        first_str = ''
        second_str = ''
        third_str = ''

        for i in words:

            for j in i:
                if j.lower() in first_row:
                    first_str += j.lower() 
                elif j.lower() in second_row:
                    second_str += j.lower()
                elif j.lower() in third_row:
                    third_str += j.lower()
            
            if first_str == i.lower() or second_str == i.lower() or third_str == i.lower():
                result.append(i)

            first_str, second_str, third_str = '', '', ''
        return result
