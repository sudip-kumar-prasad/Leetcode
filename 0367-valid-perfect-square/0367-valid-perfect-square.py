class Solution(object):
    import math
    def isPerfectSquare(self, num):
        ans = False
        for i in range(1,int(math.sqrt(num))+1):
            if i * i == num:
                ans = True
        return ans


        