class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for x,y in prerequisites:
            adj[y].append(x)
            indegree[x] +=1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodeVisited = 0
        while queue:
            node = queue.pop(0)
            nodeVisited +=1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return nodeVisited==numCourses
