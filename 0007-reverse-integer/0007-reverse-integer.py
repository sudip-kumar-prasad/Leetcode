class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        a = str(x)
        i = 0
        y = []
        d = x
        while i < len(a):
            b = d % 10
            y.append(b)
            d = d // 10
            i += 1
        ans = 0
        for i in y:
            ans = ans * 10 + i
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return sign * ans

        