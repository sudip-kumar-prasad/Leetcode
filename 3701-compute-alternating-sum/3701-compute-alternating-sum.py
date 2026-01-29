class Solution(object):
    def alternatingSum(self, nums):
        even_sum = sum(nums[::2])
        odd_sum = sum(nums[1::2])
        return even_sum - odd_sum