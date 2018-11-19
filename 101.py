# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def revtrav(self,root):
        if not root:return
        root.left,root.right=root.right,root.left
        self.revtrav(root.left)
        self.revtrav(root.right)
        return root
    #def trav(self,root):
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        chleft=self.revtrav(root.left)
        def trav(a,b):
            if not a and not b :return True
            if not a or not b:return False
            flag=False
            if a.val==b.val:
                flag=True
            return flag and trav(a.left,b.left) and trav(a.right,b.right)
        return trav(chleft,root.right)
        
