'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) + 1
            if dict.get(i) > len(nums)/2:
                return i



    '''
    just saw a great idea for solving this question.

    transform this question to the following:
        team A and team Others join a game, team A are more than half.
        We first give A one point, then they randomly show up.
        If team A show up, they get 1 point.
        If taem Others show up, they lose 1 point.
        The team who has the positive points hold the flag.
        Which team will hold the flag in the end?
    '''

'''
public class Solution {
    public int majorityElement(int[] num) {
        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;

        }
        return major;
    }
}