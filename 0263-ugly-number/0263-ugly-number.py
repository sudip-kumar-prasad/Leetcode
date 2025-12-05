class Solution(object):
    def isUgly(self, n):
        x = [2, 3, 5]

        if n <= 0:
            return False

        if n == 1:
            return True

        y = []

        i = 2
        temp = n
        while i * i <= temp:
            while temp % i == 0:
                y.append(i)
                temp //= i
            i += 1

        if temp > 1:
            y.append(temp)

        for i in y:
            if i not in x:
                return False

        return True
