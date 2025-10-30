class Solution(object):
    def maxProfit(self, k, prices):
        n=len(prices)
        ans = 0
        memo = {}
        def helper(idx,buy,t_count):
            if idx == n or t_count == k:
                return 0
            if (idx,buy,t_count) in memo:
                return memo[(idx,buy,t_count)]
            if buy:
                take = -prices[idx] + helper(idx+1,not buy,t_count)
                not_take = helper(idx+1, buy,t_count)
                ans = max(take,not_take)
            else:
                take = prices[idx] + helper(idx+1,not buy,t_count+1)
                not_take = helper(idx+1,buy,t_count)
                ans = max(take,not_take)
            memo[(idx,buy,t_count)] = ans
            return ans
        return helper(0,True,0)
        