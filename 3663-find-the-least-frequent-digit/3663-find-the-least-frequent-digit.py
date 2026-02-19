class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = list(map(int, str(n)))
        d = {}
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        min_freq = min(d.values()) 
        c = []
        for i in d:
            if d[i] == min_freq:
                c.append(i)
        return min(c)
        

        