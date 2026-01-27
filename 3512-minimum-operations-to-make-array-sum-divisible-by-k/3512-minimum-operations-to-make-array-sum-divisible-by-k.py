class Solution(object):
    def minOperations(self, nums, k):
        res = sum(nums)
        return res%k

        