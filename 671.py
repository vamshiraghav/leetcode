# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        if not root:return -1
        if not root.left and not root.right:return -1
        a=root.val
        s=set([a,root.left.val,root.right.val])
        if len(s)==1:return -1
        if len(s)==3:return min(root.left.val,root.right.val)
        print("here")
        if len(s)==2:return root.left.val if root.left.val!=root.val else root.right.val
        #return min(root.left.val,root.right.val)
        """
        a=set()
        def trav(root):
            if not root:return
            a.add(root.val)
            trav(root.left)
            trav(root.right)
        trav(root)
        b=list(a)
        b.sort()
        if len(b)<=1:return -1
        return b[1]
            
               
            
        
