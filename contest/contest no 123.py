#question number #989

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a=''.join([str(x) for x in A])
        a=int(a)
        a+=K
        a=str(a)
        return [ int(x) for x in a]
