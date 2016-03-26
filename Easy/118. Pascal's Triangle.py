'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
# my solution
import operator as op
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                tmp.append(self.ncr(i,j))
            result.append(tmp)
        return result

    def ncr(self, n, r):
        r = min(r, n-r)
        if r == 0: return 1
        numer = reduce(op.mul, xrange(n, n-r, -1))
        denom = reduce(op.mul, xrange(1, r+1))
        return numer//denom



    # # an amazing solution:
    # def generate(self, numRows):
    # res = [[1]]
    # for i in range(1, numRows):
    #     res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    # return res[:numRows]

    # # explanation: Any row can be constructed using the offset sum of the previous row. Example:
    #  #    1 3 3 1 0
    #  # +  0 1 3 3 1
    #  # =  1 4 6 4 1