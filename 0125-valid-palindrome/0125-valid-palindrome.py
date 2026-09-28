class Solution(object):
    def isPalindrome(self,s):
        # if s == " ":
        #     return True
        t1 = ''
        a = s[::-1]
        b = a.split()
        ans1 = ('').join(b)
        for i in ans1:
            if i.isalpha() or i.isdigit():
                t1 += i 
        print(t1)

        t2 = ''  
        x = s.split()
        y = ('').join(x)
        for i in y:
            if i.isalpha() or i.isdigit():
                t2 += i
        print(t2)

        if t1.lower() == t2.lower():
            return True
        return False

        