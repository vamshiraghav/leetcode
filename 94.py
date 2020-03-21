# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l=[]
        if not root:return l
        a=self.inorderTraversal(root.left)
        b=[root.val]
        c=self.inorderTraversal(root.right)
        return l+a+b+c
        
        
