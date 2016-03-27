'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        return self.go(root,1,result)

    def go(self,root,level,result):
        if root:
            if len(result) < level:
                result.append([root.val])
            else:
                result[level-1].append(root.val)
            if root.left:
                result = self.go(root.left, level+1, result)
            if root.right:
                result = self.go(root.right, level+1, result)
        return result