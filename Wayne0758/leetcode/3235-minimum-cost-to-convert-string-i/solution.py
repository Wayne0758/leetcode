class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        hashmap = defaultdict(dict)
        distgrid = [[float("inf")]*26 for _ in range(26)]
        for i in range(len(original)):
            distgrid[ord(original[i])-ord('a')][ord(changed[i])-ord('a')] = min(distgrid[ord(original[i])-ord('a')][ord(changed[i])-ord('a')], cost[i])
        for i in range(26):
            distgrid[i][i] = 0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distgrid[i][j] = min(distgrid[i][j], distgrid[i][k] + distgrid[k][j])
        res = 0
        for i in range(len(source)):
            if distgrid[ord(source[i])-ord('a')][ord(target[i])-ord('a')] == float("inf"):
                return -1
            res += distgrid[ord(source[i])-ord('a')][ord(target[i])-ord('a')]
        return res
