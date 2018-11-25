class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<=0:
            return len(A)
        if len(set(A))==len(A):return 0
        dic={}
        for i in A:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        b=set(A)
        #b.sort()
        count=0
        for i in dic:
            if dic[i]>1:
                for j in range(dic[i]-1):
                    tempc=1
                    while True:
                        if (i+tempc) in b:
                            tempc+=1
                        else:
                            b.add(i+tempc)
                            count+=tempc
                            break
        return count
