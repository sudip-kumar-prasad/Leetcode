class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])

        curr_end = float('-inf')
        c = 0

        for start,end in pairs:
            if start>curr_end:
                c+=1
                curr_end = end 

        return c
        