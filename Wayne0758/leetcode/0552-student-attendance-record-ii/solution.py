class Solution:
    def checkRecord(self, n: int) -> int:
        kmod = 10**9 + 7
        
        def count(n):
            if n == 1:
                return {(0, 0): 1, (0, 1): 1, (0, 2): 0,
                        (1, 0): 1, (1, 1): 0, (1, 2): 0}
            tmp = count(n-1)
            res = collections.defaultdict(int)

            res = {(0, 0): (tmp[(0, 0)]+tmp[(0, 1)]+tmp[(0, 2)]) % kmod, (0, 1): tmp[(0, 0)] % kmod, (0, 2): tmp[(0, 1)] % kmod,
                    (1, 0): (tmp[(0, 0)]+tmp[(0, 1)]+tmp[(0, 2)]+tmp[(1, 0)]+tmp[(1, 1)]+tmp[(1, 2)]) % kmod, (1, 1): tmp[(1, 0)] % kmod, (1, 2): tmp[(1, 1)] % kmod}
            return res
        res = count(n)
        ans = 0
        for k in res.values():
            ans+=k
        return ans % kmod

