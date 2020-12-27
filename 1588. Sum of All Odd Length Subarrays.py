class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        result=0
        for i in range(n):
            startSubArray=n-i
            endSubArray=i+1
            total = startSubArray*endSubArray
            odd = (total+1)//2
            # print(odd)
            result+=odd*arr[i]
        return result
