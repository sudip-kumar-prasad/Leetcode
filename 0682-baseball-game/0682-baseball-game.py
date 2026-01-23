class Solution(object):
    def calPoints(self, operations):
        x = []
        for i in range(len(operations)):
            if operations[i] == "C":
                x.pop()
            elif operations[i] == "D":
                s = x[-1] * 2
                x.append(s)
            elif operations[i] == "+":
                n = x[-1] + x[-2]
                x.append(n)
            else:
                x.append(int(operations[i]))
        return sum(x)
        