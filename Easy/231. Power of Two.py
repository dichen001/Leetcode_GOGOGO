#Given an integer, write a function to determine if it is a power of two.
import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        x = math.log(n,2)
        return abs(round(x) - x) < 0.0000000000001
