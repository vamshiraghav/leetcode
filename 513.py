# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trav(self,root,level):
        if not root:return
        self.trav(root.left,level+1)
        self.trav(root.right,level+1)
        if self.m<level:
            self.m=level
            self.val=root.val
        #print(root.val)
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return
        self.m=-1
        self.val=None
        self.trav(root,0)
        return self.val
        
