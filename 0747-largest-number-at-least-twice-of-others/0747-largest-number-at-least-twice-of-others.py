class Solution(object):
    def dominantIndex(self, nums):
        max_num = max(nums)
        y = nums.index(max_num)
        nums.remove(max_num)
        x = []
        for i in range(len(nums)):
            if nums[i]*2 <= max_num:
                x.append(nums[i])
        if len(nums) == len(x):
            return y
        else:
            return -1


        