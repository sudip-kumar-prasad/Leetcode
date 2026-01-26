class Solution(object):
    def findLucky(self, arr):
        x = {}
        for i in arr:
            if i in x:
                x[i] += 1 
            else:
                x[i] = 1
        ans = -1
        for num in x:
            if num == x[num]:
                ans = max(ans, num)

        return ans