class Solution(object):
    def minElement(self, nums):
        ans = []
        for i in nums:
            s = 0
            for j in str(i):
                s += int(j)
            ans.append(s)
        return min(ans)

        