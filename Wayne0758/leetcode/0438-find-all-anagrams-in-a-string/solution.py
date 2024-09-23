class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        sn = len(s)
        pn = len(p)
        if sn < pn:
            return []

        p_count = Counter(p)
        s_count = Counter()
        for i in range(sn):
            s_count[s[i]] +=1

            if i >= pn:
                if s_count[s[i-pn]] == 1:
                    del s_count[s[i-pn]]
                else:
                    s_count[s[i-pn]]-=1
            if p_count == s_count:
                res.append(i-pn+1)
        return res
