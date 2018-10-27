# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trav(self,root):
        if not root:
            return 0
        return self.trav(root.left)+self.trav(root.right)
    def nz(self,i):
        if not i:
            return 0
        return i.val
    def sumnodes(self,a,b,ret):
        if not a and not b:
            return None
        ret.val=(self.nz(a)+self.nz(b))
        print(ret.left)
        ret.left=TreeNode(self.nz(0 if a else a.left) +self.nz(0 if b else b.left))
        ret.right=TreeNode(self.nz(0 if a else a.right)+self.nz(0 if b else b.right))
        self.sumnodes( a and a.left,b and b.left,ret.left)
        self.sumnodes(a and a.right,b and b.right,ret.right)
        return ret
    
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right= self.mergeTrees(t1.right,t2.right)
            return t1
        else:
            return t1 or t2
        
        
        
        
