class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        res = []
        for st in strs:
            hashmap[tuple(sorted(list(st)))].append(st)
        for l in hashmap.values():
            res.append(l)
        return res
