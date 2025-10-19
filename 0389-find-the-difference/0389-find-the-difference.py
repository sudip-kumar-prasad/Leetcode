class Solution(object):
    def findTheDifference(self, s, t):
        res = 0
        for i in s+t:
            res ^= ord(i)
        return chr(res)