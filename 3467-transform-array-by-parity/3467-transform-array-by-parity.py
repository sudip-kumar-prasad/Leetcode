class Solution(object):
    def transformArray(self, nums):
        res = []
        for i in nums:
            if i%2 == 0:
                res.append(0)
            else:
                res.append(1)
        return sorted(res)
        