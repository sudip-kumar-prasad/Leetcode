class Solution(object):
    def mirrorDistance(self, n):
        a = str(n)
        x = a.split()
        res = int(x[0][::-1])
        return abs(n-res) 
        
        