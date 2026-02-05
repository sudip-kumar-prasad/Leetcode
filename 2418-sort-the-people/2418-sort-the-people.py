class Solution:
    def sortPeople(self, names, heights):
        n = len(heights)

        indices = list(range(n))

        for i in range(n):
            for j in range(0, n - i - 1):
                if heights[indices[j]] < heights[indices[j + 1]]:
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]

        result = []
        for i in indices:
            result.append(names[i])

        return result
