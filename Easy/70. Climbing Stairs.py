'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Subscribe to see which companies asked this question
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        step1 = 1
        step2 = 2
        all = 0
        if n <= 2:
            return n
        else:
            for i in range(2,n):
                all = step1 + step2
                step1 = step2
                step2 = all
        return all
        '''
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

# note: Fibonacci.   read this post:  https://leetcode.com/discuss/16866/basically-its-a-fibonacci

# What a smart way to solve it. Why didn't I think of it.