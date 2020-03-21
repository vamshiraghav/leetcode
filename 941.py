class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<2:return False
        mid=A.index(max(A))
        l=len(A)
        if mid==0 or mid==l-1:return False
        for i in range(mid):
            if not A[i]<A[i+1]:return False
        for i in range(mid,l-1):
            if not A[i]>A[i+1]:return False
        return True
        
