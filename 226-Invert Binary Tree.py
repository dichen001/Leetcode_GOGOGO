# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        ## method 1: recursive
        '''
        if root == None:
            return root
        else:
            # because invertTree is a class method, you have to use that class to call it!
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''

        ## method 2: iterative DFS
        '''
        stack = [root]
        while stack != []:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
        '''

        ## method 3: iterative BFS
        if root is None:
            return root
        parent = [root]
        while parent!=[]:
            children = []
            for node in parent:
                node.left, node.right = node.right, node.left
                if(node.left): children.append(node.left)
                if(node.right): children.append(node.right)
            parent = children

        return root