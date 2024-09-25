class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        l = l1+l2
        appeared = set()
        res = []
        for s in l:
            if s not in appeared:
                appeared.add(s)
                res.append(s)
            else:
                if s in res:
                    res.remove(s)
        return res
