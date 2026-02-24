class Solution(object):
    def differenceOfSums(self, n, m):
        div_n = 0
        ndiv_n = 0 
        for i in range(1,n+1):
            if i%m ==0 :
                div_n += i
            else:
                ndiv_n += i
        return ndiv_n - div_n
        