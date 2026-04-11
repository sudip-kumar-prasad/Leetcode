class Solution(object):
    import math
    def findGCD(self, nums):
        l = min(nums)
        h = max(nums)
        # x = []
        # y = []
        # for i in range(1,l+1):
        #     if l%i == 0:
        #         x.append(i)
        # for i in range(1,h+1):
        #     if h%i == 0:
        #         y.append(i)

        # l1 = len(x)
        # l2 = len(y)

        # res = float('-inf')
        # if l1<l2:
        #     for i in x:
        #         if i in y:
        #             if i>res:
        #                 res = i
        # else:
        #     for i in y:
        #         if i in x:
        #             if i>res:
        #                 res = i

        # return res
        while h!=0:
            l,h=h,(l%h)
        return l




        