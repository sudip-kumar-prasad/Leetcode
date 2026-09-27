class Solution(object):
    def missingNumber(self, nums):
        s = sum(nums)
        l = len(nums)
        n = l * (l+1) / 2
        return n - s
        