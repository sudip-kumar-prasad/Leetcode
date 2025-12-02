class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        n = numCourses   
        dp = [[False] * n for _ in range(n)]
        for u, v in prerequisites:
            dp[u][v] = True
        for k in range(n):
            for i in range(n):
                if dp[i][k]:               
                    for j in range(n):
                        dp[i][j] = dp[i][j] or dp[k][j]
        return [dp[u][v] for u, v in queries]
