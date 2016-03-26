'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        label = 1
        for i in range(len(digits))[::-1]:
            if label == 1:
                digits[i] = (digits[i]+1) % 10
                if digits[i] > 0:
                    label = 0
        if label == 1:
            digits.insert(0,1)
        return digits

        