class Solution(object):
    def findLucky(self, arr):
        x = {}
        for i in arr:
            if i in x:
                x[i] += 1 
            else:
                x[i] = 1
        ans = -1
        for i in x:
            if i == x[i]:
                ans = max(ans, i)

        return ans