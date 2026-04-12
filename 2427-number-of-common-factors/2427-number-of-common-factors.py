class Solution(object):
    def commonFactors(self, a, b):
        f1 = []
        f2 = []
        for i in range(1,a+1):
            if a%i == 0:
                f1.append(i)
        for i in range(1,b+1):
            if b%i == 0:
                f2.append(i)
        res = []
        if len(f1) < len(f2):
            for i in f1:
                if i in f2:
                    res.append(i)
        else:
            for i in f2:
                if i in f1:
                    res.append(i)
        return len(res)

        