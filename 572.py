# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def issame(self,a,b):
        if not a and not b:return True
        if not a or not b:return False
        if not a.val==b.val:return False
        return self.issame(a.left,b.left) and self.issame(a.right,b.right)
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:return True
        if not s or not t:return False
        return self.issame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
