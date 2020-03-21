class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a={}
        for i in nums:
            if i not in a:a[i]=1
            else:
                a[i]+=1
        #a.sort()
        m=0
        nsetl=list(set(nums))
        nsetl.sort()
        for i in range(len(nsetl)-1):
            m=max(m,a[nsetl[i]]+a[nsetl[i+1]]) if abs(nsetl[i+1]-nsetl[i])==1 else m 
        return m
