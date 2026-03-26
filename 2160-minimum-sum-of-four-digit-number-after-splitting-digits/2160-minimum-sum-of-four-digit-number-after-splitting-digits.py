class Solution(object):
    def minimumSum(self, num):
        res = []
        for i in str(num):
            res.append(int(i))
        res.sort()
        num1 = res[0]*10 + res[2]
        num2 = res[1]*10 + res[3]
        return num1 + num2
