"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.dic={}
    def trav(self,root,level):
        if not root:
            return 0
        if level in self.dic:
            self.dic[level].append(root.val)
        else:
            self.dic[level]=[root.val]
        for i in root.children:
            self.trav(i,level+1)
        #return 1+self.trav(root.left,level+1)+self.trav(root.right,level+1)
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.trav(root,1)
        ret=[]
        for i in self.dic:
            ret.append(self.dic[i])
        #print(self.dic,ret)
        return ret
        
