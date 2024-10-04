class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashmap = collections.defaultdict(set)
        for point in points:
            hashmap[point[0]].add(point[1])
        dict_x = {x: set_y for x, set_y in hashmap.items() if len(set_y) > 1}
        min_area = float('inf')
        for x1, x2 in combinations(dict_x.keys(), 2):
            for y1, y2 in combinations(dict_x[x1] & dict_x[x2], 2):
                min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
        return min_area if min_area < float('inf') else 0
