class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l=len(S)
        list=range(l+1)
        res=[]
        first,last=0,l
        for i in S:
            if i in "I":
                res.append(list[first])
                first+=1
            else:
                res.append(list[last])
                last-=1
        res.append(list[first])
        return res
        
