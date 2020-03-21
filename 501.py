# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trav(self,root):
        if not root:return
        if root.val not in self.list:
            self.list[root.val]=1
        else:self.list[root.val]+=1
        self.trav(root.left)
        self.trav(root.right)
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.list={}
        self.trav(root)
        res=[]
        m=0
        for i in self.list:
            if m==0:
                m=self.list[i]
                res=[i]
                continue
            if m<self.list[i]:
                res=[i]
                m=self.list[i]
            elif m==self.list[i]:
                res.append(i)
            
            
        return res
