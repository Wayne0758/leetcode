class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        a=1
        while True:
            maxim= a**x
            if maxim>n:
                break
            a+=1
        nums=[i**x for i in range(1,maxim+1)]
        f=[0] * (n+1)
        f[0]=1
        mod = 10**9+7
        for v in nums:
            for i in range(n, v-1, -1):
                f[i] += f[i-v]
                if f[i] >= mod:
                    f[i] -= mod
        return f[n]
