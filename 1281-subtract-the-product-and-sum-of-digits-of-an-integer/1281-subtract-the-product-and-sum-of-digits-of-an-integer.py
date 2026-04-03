class Solution(object):
    def subtractProductAndSum(self, n):
        x = str(n)
        mul = 1
        add = 0
        for i in x:
            mul *= int(i)
            add += int(i)
        return mul - add