class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        hashmap=collections.defaultdict(set)
        for subc in sub:
            hashmap[subc].add(subc)
        for mapping in mappings:
            hashmap[mapping[0]].add(mapping[1])
        flag=0
        tmp=1
        for start in range(len(s) - len(sub) + 1):
            if all(c_from_s in hashmap[c_from_sub] for c_from_s, c_from_sub in zip(s[start:start+len(sub)], sub)):
                return True
        return False
