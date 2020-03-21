class Solution:
    def dailyTemperatures(self, T) :
        waitDaysForWarmness = []
        stack = []
        for j,i in enumerate(T):
            while stack and stack[-1][1] <i:
                refIndex = stack.pop()[0]
                waitDaysForWarmness[refIndex]=j-refIndex
            stack.append([len(waitDaysForWarmness),i])
            waitDaysForWarmness.append(0)
        return waitDaysForWarmness

