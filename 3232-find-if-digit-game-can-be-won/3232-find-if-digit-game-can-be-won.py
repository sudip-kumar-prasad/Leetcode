class Solution(object):
    def canAliceWin(self, nums):
        s = 0
        d = 0
        for i in nums:
            x = str(i)
            if len(x) == 1:
                s += int(i)
            else:
                d += int(i)
        return s > d or d > s
    

        