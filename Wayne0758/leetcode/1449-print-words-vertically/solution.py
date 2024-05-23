class Solution:
    def printVertically(self, s: str) -> List[str]:
        p=0
        pmax=0
        for c in s:
            if c==' ':
                pmax=max(p,pmax)
                p=0
            else:
                p+=1
        pmax=max(p,pmax)
        txts=s.split(' ')
        res=['' for _ in range(pmax)]
        for txt in txts:
            tmp=0
            for i in range(len(txt)):
                res[tmp]+=txt[i]
                tmp+=1
            while tmp != pmax:
                res[tmp]+=' '
                tmp+=1
        for i in range(len(res)-1,-1,-1):
            if res[i][-1] != ' ':
                return res
            while res[i][-1] == ' ':
                res[i] = res[i][:-1]
        return res
