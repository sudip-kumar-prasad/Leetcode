class Solution(object):
    def totalMoney(self, n):
        total = 0
        start = 1

        for i in range(n):
            total += start + (i % 7)

            if i % 7 == 6:
                start += 1

        return total
        