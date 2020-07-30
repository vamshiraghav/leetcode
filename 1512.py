class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=0
        noIdenticalPairs = 0
        for x in dict:
            y=dict[x]
            noIdenticalPairs+=y*(y+1)//2
        
        return noIdenticalPairs