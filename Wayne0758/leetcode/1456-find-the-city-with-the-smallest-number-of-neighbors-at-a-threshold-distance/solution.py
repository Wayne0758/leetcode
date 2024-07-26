class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        hashmap = defaultdict(dict)
        for edge in edges:
            hashmap[edge[0]][edge[1]] = edge[2]
            hashmap[edge[1]][edge[0]] = edge[2]
        desdict = defaultdict(dict)
        destmp = math.inf
        for i in range(n):
            visited = [i]
            unvisited = set(j for j in range(n))
            unvisited.remove(i)
            dijkstra = [math.inf for _ in range(n)]
            dijkstra[i] = 0
            copied_hashmap = deepcopy(hashmap)
            for j in range(n):
                for key in copied_hashmap[visited[-1]].keys():
                    if copied_hashmap[visited[-1]][key] + dijkstra[visited[-1]] < dijkstra[key]:
                        dijkstra[key] = copied_hashmap[visited[-1]][key] + dijkstra[visited[-1]]
                        del copied_hashmap[key][visited[-1]]
                del copied_hashmap[visited[-1]]
                if copied_hashmap == {}:
                    break
                tmp = math.inf
                minv = -1
                for v in unvisited:
                    if dijkstra[v] < tmp:
                        minv = v
                        tmp = dijkstra[v]
                if minv != -1:
                    unvisited.remove(minv)
                    visited.append(minv)
            des = 0
            for dist in dijkstra:
                if dist <= distanceThreshold:
                    des += 1
            desdict[des] = i
            if des < destmp:
                destmp = des
        return desdict[destmp]
