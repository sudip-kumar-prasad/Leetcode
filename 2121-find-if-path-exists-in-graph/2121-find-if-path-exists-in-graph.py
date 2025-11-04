class Solution(object):
    from collections import deque
    def validPath(self, n, edges, source, destination):
        adj = [[] for i in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n

        dq = deque()
        dq.append(source)
        visited[source] = 1

        while dq:
            p = dq.popleft()
            if p == destination:
                return True

            for i in adj[p]:
                if visited[i] == 0:
                    visited[i] = 1
                    dq.append(i)

        return False

        