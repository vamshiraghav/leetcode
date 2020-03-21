class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count=0
        l=len(A)
        if l==0 or l==1 :return 0
        sl=len(A[0])
        for i in range(sl):
            flag=True
            for j in range(l-1):
                if not ord(A[j][i])<=ord(A[j+1][i]):
                    flag=False
            if not flag:count+=1
        return count
                
