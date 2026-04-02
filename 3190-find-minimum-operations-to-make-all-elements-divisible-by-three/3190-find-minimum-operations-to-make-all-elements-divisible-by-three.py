class Solution(object):
    def minimumOperations(self, nums):
        x = []
        for i in nums:
            x.append(i%3)
        ans = 0
        for i in x:
            if i != 0:
                ans += 1
        return ans
        