class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [i+1 for i in range(n)]
        res = sorted(res,key = lambda x:str(x))
        return res
