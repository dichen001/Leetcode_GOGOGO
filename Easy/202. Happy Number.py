'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def go(n):
            sum = 0
            while n:
                i = n % 10
                sum = sum + i*i
                n = n / 10
            return sum

        slow = go(n)
        fast = go(slow)
        while slow != fast:
            slow = go(slow)
            fast = go(go(fast))
        return slow == 1

