class Solution(object):
    def isSameAfterReversals(self, num):
        x = str(num)
        s = x[::-1]
        m = int(s)
        d = str(m)
        ans = d[::-1]
        ans = int(ans)
        if ans == num:
            return True
        else:
            return False        