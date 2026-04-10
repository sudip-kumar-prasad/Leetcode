class Solution(object):
    def differenceOfSum(self, nums):
        s = 0
        n = sum(nums)
        for i in nums:
            x = str(i)
            for i in x:
                s += int(i)
        return abs(s-n)