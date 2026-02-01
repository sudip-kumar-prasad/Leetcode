class Solution(object):
    def leftRightDifference(self, nums):
        x = len(nums)
        y = [0] * x
        if x < 2:
            return y
        y[1] = nums[0]
        for i in range(2,x):
            y[i] = y[i-1] + nums[i-1]
        nums.reverse()
        a = [0] * x
        if x < 2:
            return y
        a[1] = nums[0]
        for i in range(2,x):
            a[i] = a[i-1] + nums[i-1]
        a.reverse()
        
        ans = [0] * x
        for i in range(x):
            ans[i] = abs(y[i] - a[i])
        return ans
