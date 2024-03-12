class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        a = collections.defaultdict()
        for i in range(len(s)):
            if s[i] in order:
                if s[i] not in a.keys():
                    a[s[i]] = 1
                else:
                    a[s[i]] += 1
            else:
                res += s[i]
        for o in order:
            if o in a.keys():
                for j in range(a[o]):
                    res += o
        return res
