'''Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up
Could you do it without any loop/recursion in O(1) runtime?
'''

class Solusion():
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if num == 0:
			return 0
		else:
			return 1 + (num-1) % 9 

# Notes:  -1 % 9 = 8 in Python. NOT -1.

# reference:  Digital_root   https://en.wikipedia.org/wiki/Digital_root

