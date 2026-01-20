class Solution(object):
    def findRelativeRanks(self, score):
        x = sorted(score)
        x.reverse()
        y = []
        for i in range(len(score)):
            if score[i] in x:
                s = x.index(score[i])
                y.append(s)
        ans = []
        for i in y:
            if i == 0:
                ans.append("Gold Medal")
            elif i == 1:
                ans.append("Silver Medal")
            elif i == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(i+1))
        return ans
            