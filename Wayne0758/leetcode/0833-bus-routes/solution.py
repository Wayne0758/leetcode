class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                adj[routes[i][j]].append(i)
        visited = set()
        queue = []
        for route in adj[source]:
            queue.append(route)
            visited.add(route)
        buscount = 1
        while queue:
            n = len(queue)

            for i in range(n):
                route = queue.pop(0)

                for stop in routes[route]:
                    if stop == target:
                        return buscount
                    
                    for nextroute in adj[stop]:
                        if nextroute not in visited:
                            visited.add(nextroute)
                            queue.append(nextroute)
            buscount+=1
        return -1
