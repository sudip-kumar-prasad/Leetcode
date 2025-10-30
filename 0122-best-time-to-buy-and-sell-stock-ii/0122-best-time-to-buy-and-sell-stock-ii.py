class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        ans = 0
        memo = {}
        def helper(idx,buy):
            if idx == n:
                return 0
            if (idx,buy) in memo:
                return memo[(idx,buy)]
            if buy:
                take = -prices[idx] + helper(idx+1,not buy)
                not_take = helper(idx+1, buy)
                ans = max(take,not_take)
            else:
                take = prices[idx] + helper(idx+1,not buy)
                not_take = helper(idx+1,buy)
                ans = max(take,not_take)
            memo[(idx,buy)] = ans
            return ans
        return helper(0,True)

        