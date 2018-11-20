# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        queue=[root]
        row=queue[0]
        res=[]
        levarr=[]
        m=float("-inf")
        while queue:
            node=queue.pop()
            m=max(m,node.val)
            if node.left:
                levarr.append(node.left)
            if node.right:
                levarr.append(node.right)
            if not queue:
                res.append(m)
                m=float("-inf")
                queue=levarr
                levarr=[]
        return res
                
        
