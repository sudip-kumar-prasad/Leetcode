class Solution(object):
    from itertools import combinations
    def findMaxConsecutiveOnes(self, nums):
        x=[]
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
            else:
                x.append(c)
                c = 0
        x.append(c)
        return max(x)
