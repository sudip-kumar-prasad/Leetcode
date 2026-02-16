class Solution(object):
    def truncateSentence(self, s, k):
        x = s.split()
        ans = []
        for i in range(k):
            ans.append(x[i])
        return " ".join(ans)


        