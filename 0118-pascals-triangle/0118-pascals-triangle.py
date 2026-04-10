class Solution(object):
    def generate(self, numRows):
        ans = []
        i=1
        while i < numRows+1:
            x = [1] * i

            if len(x) > 2:
                prev = ans[-1]
                for j in range(1, i - 1):
                    x[j] = prev[j - 1] + prev[j]

            ans.append(x)
            i += 1
        return ans
        