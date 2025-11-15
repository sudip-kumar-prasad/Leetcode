class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for j in d:
            if d[j] > len(nums) // 2:
                return j

        