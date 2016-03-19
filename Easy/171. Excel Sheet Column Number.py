'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        num = 0
        for i in range(len(s)):
            num = num + 26**(len(s)-1-i) * (ord(s[i]) - 64)   # A --- 65
        return num
        """
        return reduce(lambda x, y: x*26 + y ,[ord(i) - 64 for i in s])

# note: the difference between map() and reduce().   you can not map(f,[1]) but reduce(f,[1]), when f = lambda x,y: x+y