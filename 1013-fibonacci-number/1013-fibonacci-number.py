class Solution(object):
    def __init__(self):
        self.dp = {}
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
        


        