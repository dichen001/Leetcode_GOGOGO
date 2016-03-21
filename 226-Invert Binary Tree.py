'''Invert a binary tree.'''

class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		# method 1: recursive    scaleability problem. 
		if !root:
			return None
		else:
			root.left = invertTree(root.right)
			root.right = invertTree(root.left)
		return root

		# method 2: non-recursive    using stack
		if !root:
			return None
		else:
			

