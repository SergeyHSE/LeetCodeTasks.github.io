'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_idx = 0
        cookie_idx = 0
        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                child_idx += 1
                cookie_idx += 1
            else:
                cookie_idx += 1
        return child_idx
