# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        a=root
        node=TreeNode(val)
        while True:
            if val<root.val:
                if not root.left:
                    root.left=node
                    break
                root=root.left
            else:
                if not root.right:
                    root.right=node
                    break
                root=root.right
        return a
        
