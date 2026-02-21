class Solution(object):
    def findMaxK(self, nums):
        nums.sort(reverse=True)   
        
        for num in nums:
            if num <= 0:
                break
            if -num in nums:
                return num
                
        return -1