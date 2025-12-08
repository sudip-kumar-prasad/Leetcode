class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x : x[1])
        # print(intervals)
        ans = 0
        prev = -float("inf")
        for curr in intervals:
            if prev > curr[0]:
                ans += 1
            else:
                prev = curr[1]
        return ans
        