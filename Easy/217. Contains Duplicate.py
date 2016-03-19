
'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]:
            return False
        dict = {}
        for i in nums:
            print i
            if dict.has_key(i):
                return True
            else:
                dict[i] = 1
        return False
