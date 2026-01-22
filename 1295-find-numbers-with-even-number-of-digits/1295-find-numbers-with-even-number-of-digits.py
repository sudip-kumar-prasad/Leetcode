class Solution(object):
    def findNumbers(self, nums):
        c = []
        for i in range(len(nums)):
            c.append(len(str(nums[i])))
        ans = 0
        for i in c:
            if i%2 ==0 :
                ans+=1
        return ans
        