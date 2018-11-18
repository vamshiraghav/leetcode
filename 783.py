# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trav(self,root):
        if not root:return [10000000]
        return [root.val]+self.trav(root.left)+self.trav(root.right)
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr=self.trav(root)
        arr.sort()
        print(arr)
        m=None
        for i in range(len(arr)-2):
            if m==None:
                m=abs(arr[i]-arr[i+1])
            else:
                diff=abs(arr[i]-arr[i+1])
                if diff:
                    m=min(m,diff)
                print(m)
        return m
            
