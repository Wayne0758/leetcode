class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nandhs = zip(names,heights)
        nandhs = sorted(nandhs, key = lambda x:x[1])
        res = []
        for nandh in nandhs:
            res += [nandh[0]]
        return res[::-1]
