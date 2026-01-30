class Solution(object):
    def maximumWealth(self, accounts):
        ans = []
        for i in accounts:
            ans.append(sum(i))
        return max(ans)
        