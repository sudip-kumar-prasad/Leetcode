class Solution(object):
    def maxProduct(self, nums):
        max_nums = max(nums)
        nums.remove(max_nums)
        second_max = max(nums)
        return (max_nums-1) * (second_max-1)

        