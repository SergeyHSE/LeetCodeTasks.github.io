"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def gen_parenth(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                gen_parenth(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                gen_parenth(current + ')', open_count, close_count + 1)
        gen_parenth('', 0, 0)
        return result
