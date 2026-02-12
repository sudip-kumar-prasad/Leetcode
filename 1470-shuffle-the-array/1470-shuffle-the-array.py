class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res