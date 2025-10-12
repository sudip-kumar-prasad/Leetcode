class Solution(object):
    from collections import Counter
    def longestPalindrome(self, s):
        freq = Counter(s)
        l=0
        odd_found = False
        for i in freq.values():
            if i%2==0:
                l+=i
            else:
                l+= i-1
                odd_found = True
        if odd_found:
            l+=1
        return l



        