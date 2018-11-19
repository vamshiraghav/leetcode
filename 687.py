# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkmesame(self,root,val):
        if not root:return 0
        count=0
        if root.val==val:
            count+=1
        else:return 0
        return count+max(self.checkmesame(root.left,val),self.checkmesame(root.right,val))
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        count=0
        if root.left:
            if root.val==root.left.val:
                #count+=1
                count+=self.checkmesame(root.left,root.val)
        if root.right:
            if root.val==root.right.val:
                #count+=1
                count+=self.checkmesame(root.right,root.val)
        return max([count,self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right)])
        
