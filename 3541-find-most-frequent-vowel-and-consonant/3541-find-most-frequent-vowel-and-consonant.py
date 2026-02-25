class Solution(object):
    def maxFreqSum(self, s):
        v_c = []
        c_c = []
        for i in s:
            if i in ('a','e','i','o','u'):
                v_c.append(i)
            else:
                c_c.append(i)
        d_v = {}
        for i in v_c:
            if i in d_v:
                d_v[i] += 1
            else:
                d_v[i] = 1
        d_c = {}
        for i in c_c:
            if i in d_c:
                d_c[i] += 1
            else:
                d_c[i] = 1

        d_v_c = []
        for i,j in d_v.items():
            d_v_c.append(j)

        d_c_c = []
        for i,j in d_c.items():
            d_c_c.append(j)

        max_v = max(d_v_c) if d_v_c else 0
        max_c = max(d_c_c) if d_c_c else 0

        return max_c + max_v

                