"""
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
  """
  :type n: int
  :rtype: int
  """
  def guessNumber(self, n):
    low = 1
    high = n
    
    while low <= high:
      mid = (low + high) // 2
      result = guess(mid)
      if result == 0:
        return mid
      elif result == 1:
        low = mid + 1
      else:
        high = mid - 1
    
    return -1  # Shouldn't reach here (error case)
        
