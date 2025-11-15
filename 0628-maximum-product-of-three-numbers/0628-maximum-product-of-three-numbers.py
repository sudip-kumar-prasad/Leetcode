class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        nums.reverse()
        option1 = nums[0] * nums[1] * nums[2]
        option2 = nums[-1] * nums[-2] * nums[0]
        return max(option1, option2)
