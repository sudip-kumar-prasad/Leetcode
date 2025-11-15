class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for u,v in d.items():
            if v>1:
                return True
        return False